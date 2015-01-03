Customer Login:

Login -- http://127.0.0.1:8000/bankprocess/customerlogin/username/password/

userid will be thrown in the above request.

view transaction -- http://127.0.0.1:8000/bankprocess/trans/userid/

updating the userprofile
put :
{"id":"4","username":"arunlal","address":"test"}

Transaction credit/debit.
{"withdrawal":"0", "deposit","5000","userId","4"}
