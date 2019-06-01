# Instagram SSL Pinning
Bypass Instagram SSL Pinning on Android (`ARM and x86`) Version **95.0.0.21.124**

Requirements
------------
* Instagram APK ([ARM](https://apkpure.com/instagram/com.instagram.android/download/156514151-APK) - [x86](https://apkpure.com/instagram/com.instagram.android/download/156514161-APK))  
  ***Download only from this links, not Google Play or somewhere else***  
  
* a **rooted** Android device (Physical or virtual)  
   *[Genymotion](https://www.genymotion.com/) Android 8+ suggested.*  
   *Genymotion virtual devices is rooted by default.*
   
* ADB ([Download](https://developer.android.com/studio/releases/platform-tools.html))  
    *Genymotion will install ADB automatically and you can find it on `<Genymotion Installation path>/tools`*
  
* Latest version of JDK ([Download](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html))

* Burp Suite (***.jar version**) ([Download](https://portswigger.net/burp/communitydownload))

Usage
-----
1. Install Genymotion, your virtual device and start it.  

2. Download and install Instagram apk on your device.  

3. Run Instagram and close it.  
  ***It's important to run Instagram app once before start patching!***  
  
4. Download the patched file ([ARM](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/arm) - [x86](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/x86)) and push it to the device:  
  `adb push libliger.so /data/data/com.instagram.android/lib-zstd/libliger.so`  
  
5. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your Android device.  
    *You should [install Burp Suite certificate on your Android device](https://distributedcompute.com/2017/12/12/tech-note-installing-burp-certificate-on-android/)* 
    
6. That's it! Now open the Instagram app on your device and intercept the requests in Burp Suite !

Instagram Signature Key (v95.0.0.21.124) ARM and x86
----------------------------------------------------
`6ad7f81743171130b0202c7cdf1015ab40ed7fe438b63418e52b0e0b06139ecb`  

Non-Root Method (v72.0.0.21.98)  
-------------------------------  
**Note: Version 72.0.0.21.98 is the latest version you can use in non-root method, because in the newer versions libliger.so has been created after first app launch.**

Usage
-----
1. Download and install patched APK ([ARM](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/non-root/arm) - [x86](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/non-root/x86)).  

2. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your Android device.  
    *You should [install Burp Suite certificate on your Android device](https://distributedcompute.com/2017/12/12/tech-note-installing-burp-certificate-on-android/)* 

3. That's it! Now open the Instagram app on your device and intercept the requests in Burp Suite !  

Instagram Signature Key (v72.0.0.21.98) ARM and x86
----------------------------------------------------
`19ce5f445dbfd9d29c59dc2a78c616a7fc090a8e018b9267bc4240a30244c53b`  


Donations
--------
If you want to show your appreciation, you can donate via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=its13moji%40gmail%2ecom&lc=US&item_name=Instagram_SSL_Pinning_Donation).  
Bitcoin: `1GhTaq5HqEj4xpP42drPxT4FNzxp8zUTfK`  
Iranian users can donate via [IDPay](https://idpay.ir/itsmoji).  
  
Thanks.