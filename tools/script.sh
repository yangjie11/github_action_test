python3 main.py

if [ -z "$IS_MASTER_REPO" ]
then
        echo "User trigger, begin to check Chip Support Package."
        docker pull summergift/csp_test:v1.0
        cd ..
        docker run -v "`pwd`:/rt-thread/travisci_test" -it summergift/csp_test:v1.0 bash -c "python /rt-thread/travisci_test/tools/csp_check/csp_check.py"
        cd tools/csp_check && python3 mail_send.py
else
        echo "Master trigger, No need to check Chip Support Package."
fi
