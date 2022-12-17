//<script type=text/javascript>
    //<![CDATA[
    // declare PageMethods
    var PageMethods = function() {
        PageMethods.initializeBase(this);
        this._timeout = 0;
        this._userContext = null;
        this._succeeded = null;
        this._failed = null;
    }


    // define the mother class of PageMethods
    PageMethods.prototype = {
        _get_path: function() {
            var p = this.get_path();
            if (p) return p;
            else return PageMethods._staticInstance.get_path();
        },
    
        EncodeUserName: function(username, succeededCallback, failedCallback, userContext) {
            return this._invoke(this._get_path(), 
                                'EncodeUserName', 
                                false, 
                                {username:username}, 
                                succeededCallback, 
                                failedCallback, 
                                userContext);
        },
    
        DecodeUserName: function(username, succeededCallback, failedCallback, userContext) {
            return this._invoke(this._get_path(), 'DecodeUserName', false, {username:username}, succeededCallback,failedCallback, userContext);
        },
    
        GetFailedLoginCount: function(username, succeededCallback, failedCallback, userContext) {
            return this._invoke(this._get_path(), 'GetFailedLoginCount', false, {username:username}, succeededCallback, failedCallback, userContext);
        },
    
        GetCaptchaStatus: function(username, succeededCallback, failedCallback, userContext) {
            return this._invoke(this._get_path(), 'GetCaptchaStatus', false, {username:username}, succeededCallback, failedCallback, userContext);
        }
    }
    
    // define the PageMethods class
    PageMethods.registerClass('PageMethods', Sys.Net.WebServiceProxy);
    PageMethods._staticInstance = new PageMethods();
    PageMethods.set_path = function(value) { PageMethods._staticInstance.set_path(value); }
    PageMethods.get_path = function() { return PageMethods._staticInstance.get_path(); }
    PageMethods.set_timeout = function(value) { PageMethods._staticInstance.set_timeout(value); }
    PageMethods.get_timeout = function() { return PageMethods._staticInstance.get_timeout(); }
    PageMethods.set_defaultUserContext = function(value) { PageMethods._staticInstance.set_defaultUserContext(value); }
    PageMethods.get_defaultUserContext = function() { return PageMethods._staticInstance.get_defaultUserContext(); }
    PageMethods.set_defaultSucceededCallback = function(value) { PageMethods._staticInstance.set_defaultSucceededCallback(value); }
    PageMethods.get_defaultSucceededCallback = function() { return PageMethods._staticInstance.get_defaultSucceededCallback(); }
    PageMethods.set_defaultFailedCallback = function(value) { PageMethods._staticInstance.set_defaultFailedCallback(value); }
    PageMethods.get_defaultFailedCallback = function() { return PageMethods._staticInstance.get_defaultFailedCallback(); }
    PageMethods.set_enableJsonp = function(value) { PageMethods._staticInstance.set_enableJsonp(value); }
    PageMethods.get_enableJsonp = function() { return PageMethods._staticInstance.get_enableJsonp(); }
    PageMethods.set_jsonpCallbackParameter = function(value) { PageMethods._staticInstance.set_jsonpCallbackParameter(value); }
    PageMethods.get_jsonpCallbackParameter = function() { return PageMethods._staticInstance.get_jsonpCallbackParameter(); }
    PageMethods.set_path("login-sso.aspx");
    PageMethods.EncodeUserName = function(username,onSuccess,onFailed,userContext) {PageMethods._staticInstance.EncodeUserName(username,onSuccess,onFailed,userContext); }
    PageMethods.DecodeUserName = function(username,onSuccess,onFailed,userContext) {PageMethods._staticInstance.DecodeUserName(username,onSuccess,onFailed,userContext); }
    PageMethods.GetFailedLoginCount = function(username,onSuccess,onFailed,userContext) {PageMethods._staticInstance.GetFailedLoginCount(username,onSuccess,onFailed,userContext); }
    PageMethods.GetCaptchaStatus = function(username,onSuccess,onFailed,userContext) {PageMethods._staticInstance.GetCaptchaStatus(username,onSuccess,onFailed,userContext); }
    //]]>
//</script>
    
    
    
    
    
    
    
    
    
//<script language="javascript">
    function checkuser() {

        var strx = new String();
        var stry;

        // check username and set cookie
        strx = document.forms["LoginSSOFrm"].username.value; //strx is the username
        if (strx.length < 1) {
            alert("Please enter a username.");
            document.forms["LoginSSOFrm"].username.focus();
            return false;
        }
        else {
            // this can be separate thread not affecting below steps
            PageMethods.EncodeUserName(strx,
            function (response) { document.cookie = "CIQ_UN=" + response; });
        }

        stry = document.forms["LoginSSOFrm"].password.value; //stry is the password
        // this is the google captcha related section only
        if (document.getElementById("g-recaptcha-response") != null) {
            if (stry.length < 1) {
                alert("Please enter a password.");
                document.forms["LoginSSOFrm"].password.focus();
                return false;
            }

            var resp = grecaptcha.getResponse(widgetId2);
            if (resp == null || resp.length == 0) {
                alert("Please answer the security prompt then click Sign In.");
                return false;
            }
            else {
                document.forms["LoginSSOFrm"].action = 'https://login.spglobal.com/oam/server/auth_cred_submit';
                document.forms["LoginSSOFrm"].submit();
            }
        }
        else {
            // not postback, no captcha
            // check password & cookie
            if (stry.length < 1) {
                alert("Please enter a password.");
                document.forms["LoginSSOFrm"].password.focus();
                return false;
            }

            PageMethods.GetCaptchaStatus(strx,
            function (value) {
                //alert('pwd: ' + stry + '\n');
                if (value == 1 || value == -5) {
                    // captcha required or locked
                    //alert('value = 1 or 5, action=' + document.forms["LoginSSOFrm"].action);
                    document.forms["LoginSSOFrm"].submit();
                }
                else {
                    //go to idm
                    document.forms["LoginSSOFrm"].action = 'https://login.spglobal.com/oam/server/auth_cred_submit';
                    document.forms["LoginSSOFrm"].submit();
                }
            });
        }
        
    }
    


if (typeof (iIntervalID) != 'undefined') {
    window.clearInterval(iIntervalID);
}


function checkCookie() {

    document.cookie = "testcookie";

    if (!navigator.cookieEnabled || document.cookie.indexOf("testcookie") == -1) {
        document.getElementById("DisabledCookiesMessageDiv").style.display = '';
        if (document.forms["LoginSSOFrm"].username) {
            document.forms["LoginSSOFrm"].username.value = "";
            document.forms["LoginSSOFrm"].username.disabled = true;
        }
        if (document.forms["LoginSSOFrm"].password) {
            document.forms["LoginSSOFrm"].password.value = "";
            document.forms["LoginSSOFrm"].password.disabled = true;
        }
        if (document.getElementById("myLoginButton"))
            document.getElementById("myLoginButton").disabled = true;
        if (document.getElementById("PersistentLogin"))
            document.getElementById("PersistentLogin").disabled = true;
    }
    else {
        document.getElementById("DisabledCookiesMessageDiv").style.display = 'none';
        if (document.forms["LoginSSOFrm"].username)
            document.forms["LoginSSOFrm"].username.disabled = false;
        if (document.forms["LoginSSOFrm"].password)
            document.forms["LoginSSOFrm"].password.disabled = false;
        if (document.getElementById("myLoginButton"))
            document.getElementById("myLoginButton").disabled = false;
        if (document.getElementById("PersistentLogin"))
            document.getElementById("PersistentLogin").disabled = false;
    }
}
//</script>
