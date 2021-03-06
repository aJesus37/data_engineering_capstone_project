# Data Dictionary

## Network Logs
<sub>[Information Source](https://docs.zeek.org/en/master/script-reference/log-files.html)</sub>

- **@timestamp**: Timestamp that log was read
- **@version**: Version of the agent that shipped the data
- **@agent**: Information about the agent
    - **ephemeral_id**: Ephemeral id of the agent (changes between restarts)
    - **hostname**: Name of the host running the agent
    - **id**: Unique identifier for the agent
    - **name**: Custom name for the agent
    - **type**: Type of the agent (type of the beat)
    - **version**: Version of the agent
- **ecs**: Information about the elastic common schema
    - **version**: Version of the schema
- **host**: Information about the host
    - **name**: Host name
- **input**: Information about the input given to the agent
    - **type**: Type of the input
- **log**: Information about the log read
    - **offset**: Offset of the file that the given line was found
    - **path**: Path of the log file
- **tags**: Custom tags set on the agent
    - **element**: Tags separated as list
- **message_json**: Content of the log read
    - **AA**: The Authoritative Answer bit for response messages specifies that the responding name server is an authority for the domain name in the question section.
    - **RA**: The Recursion Available bit in a response message indicates that the name server supports recursive queries.
    - **RD**: The Recursion Desired bit in a request message indicates that the client wants recursive service for this query.
    - **TC**: The Truncation bit specifies that the message was truncated.
    - **TTLs**: The caching intervals of the associated RRs described by the answers field.
    - **Z**: A reserved field that is usually zero in queries and responses.
    - **answers**: The set of resource descriptions in the query answer.
    - **id.orig_h**: Origin Host
    - **id.orig_p**: Origin Port
    - **id.resp_h**: Response Host
    - **id.resp_p**: Response Port
    - **proto**: The transport layer protocol of the connection.
    - **query**: The domain name that is the subject of the DNS query.
    - **rcode**: The response code value in DNS response messages.
    - **rcode_name**: A descriptive name for the response code value.
    - **rejected**: The DNS query was rejected by the server.
    - **trans_id**: A 16-bit identifier assigned by the program that generated the DNS query. Also used in responses to match up replies to outstanding queries.
    - **ts**: The earliest time at which a DNS protocol message over the associated connection is observed.
    - **uid**: A unique identifier of the connection over which DNS messages are being transferred.
    - **assigned_addr**: IP address assigned by the server.
    - **client_addr**: IP address of the client. If a transaction is only a client sending INFORM messages then there is no lease information exchanged so this is helpful to know who sent the messages. Getting an address in this field does require that the client sources at least one DHCP message using a non-broadcast address.
    - **domain**: Domain given by the server in option 15.
    - **duration**: Duration of the DHCP ???session??? representing the time from the first message to the last.
    - **lease_time**: IP address lease interval.
    - **mac**: Client???s hardware address.
    - **msg_types**: The DHCP message types seen by this DHCP transaction
    - **server_addr**: IP address of the server involved in actually handing out the lease. There could be other servers replying with OFFER messages which won???t be represented here. Getting an address in this field also requires that the server handing out the lease also sources packets from a non-broadcast IP address.
    - **uids**: A series of unique identifiers of the connections over which DHCP is occurring. This behavior with multiple connections is unique to DHCP because of the way it uses broadcast packets on local networks.
    - **acks**:     Total number of ACKs seen in the previous measurement interval.
    - **gaps**: Number of missed ACKs from the previous measurement interval.
    - **peer**: In the event that there are multiple Zeek instances logging to the same host, this distinguishes each peer with its individual name.
    - **percent_lost**: Percentage of ACKs seen where the data being ACKed wasn???t seen.
    - **ts_delta**: The time delay between this measurement and the last.
    - **host**: The IP address detected running the software.
    - **name**: Name of the software (e.g. Apache).
    - **software_type**: The type of software detected (e.g. HTTP::SERVER).
    - **unparsed_version**: The full unparsed version string found because the version parsing doesn???t always work reliably in all cases and this acts as a fallback in the logs.
    - **version.major**: Major version number.
    - **version.minor**: Minor version number.
    - **notice**: Indicate if this weird was also turned into a notice.
    - **peer**: The peer that originated this weird. This is helpful in cluster deployments if a particular cluster node is having trouble to help identify which node is having trouble.
    - **source**: The source of the weird. When reported by an analyzer, this should be the name of the analyzer.
    - **conn_state**: State code for the connection
    - **duration**: How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK.
    - **history**: Records the state history of connections as a string of letters.
    - **local_orig**: If the connection is originated locally, this value will be T. If it was originated remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.
    - **local_resp**: If the connection is responded to locally, this value will be T. If it was responded to remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.
    - **missed_bytes**: Indicates the number of bytes missed in content gaps, which is representative of packet loss. A value other than zero will normally cause protocol analysis to fail but some analysis may have been completed prior to the packet loss.
    - **orig_bytes**: The number of payload bytes the originator sent. For TCP this is taken from sequence numbers and might be inaccurate (e.g., due to large connections).
    - **resp_ip_bytes**: Number of IP level bytes that the responder sent (as seen on the wire, taken from the IP total_length header field). Only set if use_conn_size_analyzer = T.
    - **resp_pkts**: Number of packets that the responder sent. Only set if use_conn_size_analyzer = T.
    - **__corrupt_record**: Captures standard error when Zeek is started from ZeekControl
    - **actions**: The actions which have been applied to this notice.
    - **msg**: The human readable message for the notice.
    - **note**: The Notice::Type of the notice.
    - **supress_for**: This field indicates the length of time that this unique notice should be suppressed.
    - **filter**: The packet filter that is being set.
    - **init**: Indicate if this is the filter set during initialization.
    - **node**: This is a string representation of the node that applied this packet filter. It???s mostly useful in the context of dynamically changing filters on clusters.
    - **success**: Indicate if the filter was applied successfully.
    - **active_dns_requests**: Current number of DNS requests awaiting a reply.
    - **active_files**: Current number of files actively being seen.
    - **active_icmp_conns**: ICMP connections currently in memory.
    - **active_tcp_conns**: TCP connections currently in memory.
    - **active_timers**: Current number of scheduled timers.
    - **active_udp_conns**: UDP connections currently in memory.
    - **bytes_recv**: Number of bytes received since the last stats interval if reading live traffic.
    - **dns_requests**: Number of DNS requests seen since last stats interval.
    - **events_proc**: Number of events processed since the last stats interval.
    - **events_queued**: Number of events that have been queued since the last stats interval.
    - **files**: Number of files seen since last stats interval.
    - **icmp_conns**: ICMP connections seen since last stats interval.
    - **mem**: Amount of memory currently in use in MB.
    - **pkt_lag**: Lag between the wall clock and packet timestamps if reading live traffic.
    - **pkts_dropped**: Number of packets dropped since the last stats interval if reading live traffic.
    - **pkts_link**: Number of packets seen on the link since the last stats interval if reading live traffic.
    - **pkts_proc**: Number of packets processed since the last stats interval.
    - **reassem_file_size**: Current size of File data in reassembly.
    - **reassem_frag_size**: Current size of packet fragment data in reassembly.
    - **reassem_tcp_size**: Current size of TCP data in reassembly.
    - **reassem_unknown_size**: Current size of unknown data in reassembly (this is only PIA buffer right now).
    - **tcp_conns**: TCP connections seen since last stats interval.
    - **timers**: Number of timers scheduled since last stats interval.
    - **udp_conns**: UDP connections seen since last stats interval.
    - **cert_chain_fuids**: The unique file IDs (fuids) of all certificates offered by the server.
    - **cipher**: SSL/TLS cipher suite that the server chose.
    - **client_cert_chain_fuids**: The unique file IDs (fuids) of all certificates requested by the client.
    - **established**: Flag to indicate if this ssl session has been established successfully, or if it was aborted during the handshake.
    - **next_protocol**: Next protocol the server chose using the application layer next protocol extension, if present.
    - **resumed**: Flag to indicate if the session was resumed reusing the key material exchanged in an earlier connection.
    - **validation_status**: Result of certificate validation for this connection.
    - **version**: SSL/TLS version that the server chose.
    - **request_body_len**: Actual uncompressed content size of the data transferred from the client.
    - **status_code**: Status code returned by the server.
    - **status_msg**: Status message returned by the server.
    - **tags**: A set of indicators of various attributes discovered and related to a particular request/response pair.
    - **trans_depth**: Track the current deepest transaction. This is meant to cope with missing requests and responses.
    - **port_num**: Port number of service
    - **port_proto**: Protocol that runs on the port
    - **service**: Service running on the port
    - **analyzers**: A set of analysis types done during the file analysis.
    - **conn_uids**: Connection UIDs over which the file was transferred.
    - **fuid**: An identifier associated with a single file.
    - **is_orig**: If the source of this file is a network connection, this field indicates if the file is being sent by the originator of the connection or the responder.
    - **md5**: An MD5 digest of the file contents.
    - **mime_type**:     A mime type provided by the strongest file magic signature match against the bof_buffer field of fa_file, or in the cases where no buffering of the beginning of file occurs, an initial guess of the mime type based on the first data seen.
    - **missing_bytes**: The number of bytes in the file stream that were completely missed during the process of analysis e.g. due to dropped packets.
    - **overflow_bytes**: The number of bytes in the file stream that were not delivered to stream file analyzers. This could be overlapping bytes or bytes that couldn???t be reassembled.
    - **rx_hosts**: If this file was transferred over a network connection this should show the host or hosts that the data traveled to.
    - **seen_bytes**: Number of bytes provided to the file analysis engine for the file.
    - **sha1**: A SHA1 digest of the file contents.
    - **timedout**: Whether the file analysis timed out at least once for the file.
    - **tx_hosts**: If this file was transferred over a network connection this should show the host or hosts that the data sourced from.
    - **level**: The severity of the reporter message. Levels are INFO for informational messages, not needing specific attention; WARNING for warning of a potential problem, and ERROR for a non-fatal error that should be addressed, but doesn???t terminate program execution.
    - **location**: This is the location in a Zeek script where the message originated. Not all reporter messages will have locations in them though.
    - **message**: An info/warning/error message that could have either been generated from the internal Zeek core or at the scripting-layer.
    - **basic_constraints.ca**: CA flag set?
    - **certificate.exponent**: Exponent, if RSA-certificate
    - **certificate.issuer**: Issuer.
    - **certificate.key_alg**: Name of the key algorithm.
    - **certificate.key_length**: Key length in bits
    - **certificate.key_type**: Key type, if key parseable by openssl (either rsa, dsa or ec)
    - **certificate.not_valid_after**: Timestamp after when certificate is not valid.
    - **certificate.not_valid_before**: Timestamp before when certificate is not valid.
    - **certificate.serial**: Serial number.
    - **certificate.sig_alg**: Name of the signature algorithm.
    - **certificate.subject**: Subject.
    - **certificate.version**: Version.
    - **id**: Unique identifier
    - **san.dns**: List of DNS entries in SAN.
    - **auth_attempts**: The number of authentication attemps we observed. There???s always at least one, since some servers might support no authentication at all. It???s important to note that not all of these are failures, since some servers require two-factor auth (e.g. password AND pubkey)
    - **client**: The client???s version string
- **dt**: Datetime
- **hr**: Hour

## Host Logs

<sub>[Information Source]()</sub>

- **@timestamp**: Timestamp that log was read
- **@version**: Version of the agent that shipped the data
- **@agent**: Information about the agent
    - **ephemeral_id**: Ephemeral id of the agent (changes between restarts)
    - **hostname**: Name of the host running the agent
    - **id**: Unique identifier for the agent
    - **name**: Custom name for the agent
    - **type**: Type of the agent (type of the beat)
    - **version**: Version of the agent
- **dt**: Date the log was read.
- **hr**: Hour the log was read.
- **client**: The initiator of a network connection for events regarding sessions, connections, or bidirectional flow records
    - **bytes**: Bytes sent from the client to the server.
    - **domain**: Client domain.
    - **ip**: IP address of the client (IPv4 or IPv6).
    - **packets**: Packets sent from the client to the server.
    - **port**: Port of the client.
- **destination**: Destination fields capture details about the receiver of a network exchange/packet.
    - **bytes**: Bytes sent from the destination to the source.
    - **domain**: Destination domain.
    - **ip**: IP address of the destination (IPv4 or IPv6).
    - **packets**: Packets sent from the destination to the source.
    - **port**: Port of the destination.
- **ecs**: Meta-information specific to ECS.
    - **version**: ECS version this event conforms to.
- **error**: These fields can represent errors of any kind.
    - **message**: Error message.
- **event**: The event fields are used for context information about the log or metric event itself.
    - **action**: The action captured by the event. This describes the information in the event.
    - **category**: A categorization value keyword used by the entity using the rule for detection of this event.
      - **element**: Each category separated as list
    - **dataset**: Name of the dataset.
    - **duration**: Duration of the event in nanoseconds.
    - **end**: event.end contains the date when the event ended or when the activity was last observed.
    - **id**: Unique ID to describe the event.
    - **kind**: This is one of four ECS Categorization Fields, and indicates the highest level in the ECS category hierarchy.
    - **module**: Name of the module this data is coming from.
    - **origin**: Source where the event originated from.
    - **outcome**: This is one of four ECS Categorization Fields, and indicates the lowest level in the ECS category hierarchy.
    - **start**: event.start contains the date when the event started or when the activity was first observed.
    - **type**: This is one of four ECS Categorization Fields, and indicates the third level in the ECS category hierarchy. 
      - **element**: Each type separated as list
- **file**: A file is defined as a set of information that has been created on, or has existed on a filesystem.
    - **ctime**: Last time the file attributes or metadata changed.
    - **extension**: File extension, excluding the leading dot.
    - **gid**: Primary group ID (GID) of the file.
    - **group**: Primary group name of the file.
    - **hash**: Hashes for the give file.
      - **sha1**: SHA1 hash.
    - **inode**: Inode representing the file in the filesystem.
    - **mime_type**: MIME type should identify the format of the file or stream of bytes using IANA official types, where possible.
    - **mode**: Mode of the file in octal representation.
    - **mtime**: Last time the file content was modified.
    - **owner**: File owner???s username.
    - **path**: Full path to the file, including the file name.
    - **setgid**: Set if the file has the setgid bit set. Omitted otherwise.
    - **setuid**: Set if the file has the setuid bit set. Omitted otherwise.
    - **size**: File size in bytes. Only relevant when file.type is "file".
    - **target_path**: Target path for symlinks.
    - **type**: File type (file, dir, or symlink).
    - **uid**: The user ID (UID) or security identifier (SID) of the file owner.
- **flow**: Netflow information 
    - **complete**: If the flow is complete
    - **final**: If the flow ended
- **group**: The group fields are meant to represent groups that are relevant to the event.
    - **id**: Unique identifier for the group on the system/platform.
    - **name**: Name of the group.
- **hash**: The hash fields represent different bitwise hash algorithms and their values.
    - **sha1**: SHA1 hash.
- **host**: A host is defined as a general computing instance.
    - **architecture**: Operating system architecture.
    - **containerized**: If host is a container
    - **hostname**: Hostname of the host.
    - **id**: Unique host id.
    - **ip**: Host ip addresses as list.
      - **element**: Each element of the list
    - **mac**: Host MAC addresses as list.
      - **element**: Each element of the list.
    - **name**: Name of the host.
    - **os**: Operating System information.
      - **family**: OS family (such as redhat, debian, freebsd, windows).
      - **kernel**: Operating system kernel version as a raw string.
      - **name**: Operating system name, without the version.
      - **platform**: Operating system platform (such centos, ubuntu, windows).
      - **type**: Use the os.type field to categorize the operating system into one of the broad commercial families.
      - **version**: Operating system version as a raw string.
- **message**: For log events the message field contains the log message, optimized for viewing in a log viewer.
- **network**: The network is defined as the communication path over which a host or network event happens.
    - **bytes**: Total bytes transferred in both directions.
    - **community_id**: A hash of source and destination IPs and ports, as well as the protocol used in a communication.
    - **direction**: Direction of the network traffic.
    - **packets**: Total packets transferred in both directions.
    - **transport**: Same as network.iana_number, but instead using the Keyword name of the transport layer (udp, tcp, ipv6-icmp, etc.).
    - **type**: In the OSI Model this would be the Network Layer. ipv4, ipv6, ipsec, pim, etc.
- **package**: These fields contain information about an installed software package.
    - **architecture**: Package architecture.
    - **description**: Description of the package.
    - **installed**: Time when package was installed.
    - **license**: License under which the package was released.
    - **name**: Package name.
    - **reference**: Home page or reference URL of the software in this package, if available.
    - **size**: Package size in bytes.
    - **type**: Type of package.
    - **version**: Package version.
- **process**: These fields contain information about a process.
    - **args**: Array of process arguments, starting with the absolute path to the executable.
      - **element**: Every element of the array.
    - **created**: Time the process was created.
    - **entity_id**: Unique identifier for the process.
    - **executable**: Absolute path to the process executable.
    - **hash**: Hashes for the executable
      - **sha1**: SHA1 hash.
    - **name**: Process name.
    - **pid**: Process ID.
    - **ppid**: Parent Process ID.
    - **start**: The time the process started.
    - **working_directory**: The working directory of the process.
- **related**:  This field set is meant to facilitate pivoting around a piece of data.
    - **ip**: All of the IPs seen on your event, as array.
      - **element**: All elements of array.
    - **user**: All the user names or other user identifiers seen on the event, as array.
      - **element**: All elements of array.
- **server**: A Server is defined as the responder in a network connection for events regarding sessions, connections, or bidirectional flow records.
    - **bytes**: Bytes sent from the server to the client.
    - **domain**: Server domain.
    - **ip**: IP address of the server (IPv4 or IPv6).
    - **packets**: Packets sent from the server to the client.
    - **port**: Port of the server.
- **service**: The service fields describe the service for or from which the data was collected.
    - **type**: The type of the service data is collected from.
- **source**: Information about the originator of the network flow.
    - **bytes**: Bytes sent from source.
    - **domain**: Source's domain.
    - **ip**: Source's IP Address (IPv4 or IPv6).
    - **packets**: Packets sent from source.
    - **port**: Port from where the connection was made.
- **system**: Information from system module.
    - **audit**: Audit information on system.
      - **host**: Host information.
        - **architecture**: Operating system architecture.
        - **boottime**: Time the system has booted up.
        - **containerized**: If the system is a container.
        - **hostname**: System's hostname.
        - **id**: System's unique identifier.
        - **ip**: System IP Addresses as array.
          - **element**: Every element in the array.
        - **mac**: Systems MAC Addresses as array.
          - **element**: Every element in the array.
        - **os**: Operating System information.
          - **family**: OS family (such as redhat, debian, freebsd, windows).
          - **kernel**: Operating system kernel version as a raw string.
          - **name**: Operating system name, without the version.
          - **platform**: Operating system platform (such centos, ubuntu, windows).
          - **type**: Use the os.type field to categorize the operating system into one of the broad commercial families.
          - **version**: Operating system version as a raw string.
        - **timezone.name**: Name of the system's timezone.
        - **timezone.offset.sec**: Time offset in seconds of the system's timezone compared to UTC.
        - **uptime**: Time the system is up.
      - **package**: These fields contain information about an installed software package.
        - **arch**: Package architecture.
        - **entity_id**: Unique identifier for the package.
        - **installtime**: Timestamp where the package was installed.
        - **license**: Package's license.
        - **name**: Package name.
        - **release**: Release number of package.
        - **size**: Package size in bytes.
        - **summary**: Description of the package.
        - **url**: Package's URL.
        - **version**: Package version number.
      - **socket**: Network information
        - **egid**: Socket ephemeral ID.
        - **euid**: Socket ephemeral unique ID.
        - **gid**: Socket's group identifier
        - **kernel_sock_address**: Socket's Kernel Address.
        - **uid**: Socket's unique identifier.
      - **user**: The user fields describe information about the user that is relevant to the event.
        - **dir**: Home directory for user.
        - **gid**: User group ids.
        - **group**: User group array
          - **element**: Elements from the array
            - **gid**: Element's groupID
            - **id**: Element's ID
            - **name**: Element's name
        - **name**: User name
        - **password**: User password information
          - **last_changed**: Last time password was changed.
          - **type**: A user???s password type.
        - **shell**: Program to run at login.
        - **uid**: User ID.
        - **user_information**: General user information. On Linux, this is the gecos field.
- **tags**: Custom tags as array
    - **element**: Every element in the array
- **user**: Information about user related to event.
    - **effective**: Effective (no alias) information
      - **group**: Groups user is in
        - **id**: Group IDs 
      - **id**: User ID
    - **entity_id**: Internal user ID to auditbeat
    - **group**: User Groups
      - **id**: User group IDs
      - **name**: User group Names
    - **id**: User ID
    - **name**: User name
    - **saved**: Cached user information
      - **group**: Groups
        - **id**: Group IDs
      - **id**: User ID
    - **terminal**: Login shell