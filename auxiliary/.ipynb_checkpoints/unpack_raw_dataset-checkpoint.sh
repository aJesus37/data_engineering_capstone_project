SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

gunzip -r $SCRIPT_DIR/../filebeat/logs
gunzip -r $SCRIPT_DIR/../auditbeat/logs