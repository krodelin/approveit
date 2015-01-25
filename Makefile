copy_capp:
	cp -vfR ../approveitCapp/Build/Release/approveitCapp/* static/

pip_freeze:
	pip freeze > requirements.txt