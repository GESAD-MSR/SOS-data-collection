docker run --rm -it \
    -p 8080:8080 \
	-v  `pwd`/../../../client:/client/ \
	alan/sos_client:0.1.0 \
	/bin/bash
