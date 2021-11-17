import os, findspark, re
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

findspark.init()


def create_spark_session():
    """Create the spark session that enables spark to process data"""
    spark = SparkSession \
        .builder \
        .getOrCreate()

    return spark

def process_network_logs(output_path, spark):
    """Process Network logs, transform fields into searchable ones and \
    convert into parquet"""
    # Read raw JSON logs into dataframe
    df_network_logs_transient = spark.read.json('filebeat/logs')
    # Creates schema for JSON field to be transformed into a structure, so it's
    # fields can also be searched on
    json_schema = spark.read.json(df_network_logs_transient.rdd.map(lambda row: row.message)).schema
    df_network_logs_final = df_network_logs_transient.withColumn('message_json',\
                                                   f.from_json(f.col('message'),\
                                           json_schema)).drop(f.col('message'))
    # Write final data as parquet, partitioned by date and hour
    df_network_logs_final.write\
    .partitionBy('dt','hr')\
    .parquet(output_path)


def process_host_logs(output_path, spark):
    """Process Host logs and convert them into parquet files"""
    # Read raw JSON logs into dataframe
    df_host_logs = spark.read.json('auditbeat/logs')
    
    # Write final data as parquet, partitioned by date and hour
    df_host_logs.write\
    .partitionBy('dt','hr')\
    .parquet(output_path)

def row_number_check(df, path):
    """Quality check for the number of rows in the resulting dataset"""
    row_count = df.count()
    if row_count < 1:
        print(f"Data Quality Failed, number of rows lesser than 1, {row_count}")
        return False
    else:
        print(f"[+] Data Quality Check 1 Passed for {path}, row_count: {row_count} [+]")
        return True

def consistency_network_quality_check(df, spark, path):
    """Consistency quality check for the resulting network dataset
    
    Explanation: Network logs is a dataset formed from many other files, 
    but all the files derivate from conn.log, so, conn.log should ALWAYS
    be the one with most hits from the list"""
    df2 = df.select('*','log.path')
    higher_path = df2.groupBy('path').count().sort(f.col('count').desc()).collect()[0]['path']

    if higher_path != '/opt/zeek/logs/current/conn.log':
        print("Path with most hits was not the conn.log: ", higher_path)
        return False
    else:
        print(f"[+] Data Quality Check 2 Passed for {path}, result is {higher_path} [+]")
        return True


def consistency_host_quality_check(df, spark, path):
    """Consistency quality check for the resulting host dataset
    
    Explanation: The network used to generate this data has mostly Linux hosts, so, in the field
    containing the operating system name, the one that should appear more should contain Linux
    on it's name, even if non-Linux hosts are added to it. Having the top hitter as Linux means
    the results are realiable and consistent to the reality."""
    df2 = df.select('host.os.*')
    higher_os_name = df2.groupBy('name').count().sort(f.col('count').desc()).collect()[0]['name']

    try:
        penguin = re.search('.*([Ll]inux).*',higher_os_name).group(1)
        if penguin == "Linux" or penguin == "linux":
            print(f"[+] Data Quality Check 2 Passed for {path}, result is {higher_os_name} [+]")
            return True
        else:
            return False
    except:
        return False


def run_quality_checks(path, spark):
    """Run all quality checks for the given path"""
    # Test number one: Guarantee that atleast 1 row of data exists in the newly
    # generated dataset
    dataframe = spark.read.parquet(path)
    test_1 = row_number_check(dataframe, path)
    # Test number two: Consistent check based on the type of data being analyzed

    # Define which test to run
    try:
        if bool(re.search('.*(network).*',path).group(1)):
            test_2 = consistency_network_quality_check(dataframe, spark, path)
        else:
            test_2 = consistency_host_quality_check(dataframe, spark, path)
    except:
        test_2 = consistency_host_quality_check(dataframe, spark, path)

    if test_1 and test_2:
        print(f"[+] All checks have passed for path {path}, ending... [+]")
    else:
        raise Exception(f"One or more of the tests failed for path {path}. Test 1: {test_1}, Test 2: {test_2}")

def main():
    """Runs all the functions defined in the ETL process."""
    NETWORK_OUTPUT_PATH='datalake/network_logs'
    HOST_OUTPUT_PATH='datalake/host_logs'
    spark = create_spark_session()

    process_network_logs(NETWORK_OUTPUT_PATH, spark)
    process_host_logs(HOST_OUTPUT_PATH, spark)
    print("\n")
    run_quality_checks(NETWORK_OUTPUT_PATH, spark)
    run_quality_checks(HOST_OUTPUT_PATH, spark)

if __name__ == "__main__":
    main()