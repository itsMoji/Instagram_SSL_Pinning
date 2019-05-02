# Instagram SSL Pinning
Bypass Instagram SSL Pinning on Android (`ARM and x86`) Version **91.0.0.18.118**

Requirements
------------
* Instagram APK ([ARM](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-instagram-91-0-0-18-118-152367-release/instagram-91-0-0-18-118-2-android-apk-download/) - [x86](https://apkpure.com/instagram/com.instagram.android/download/152367530-APK))  

* a **rooted** android device (Physical or virtual)  
   *[Genymotion](https://www.genymotion.com/) Android 7+ suggested.*  
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
  
5. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your android device.  

6. That's it! Now open the Instagram app on your device and intercept the requests in Burp Suite !

Instagram Signature Key (v91.0.0.18.118) ARM and x86
-------------------------------------------
`7f2efba692e18dd385499a6727ad440a959d575568d5547594cc54c3ff5bbe35`

Donations
--------
If you want to show your appreciation, you can donate via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=its13moji%40gmail%2ecom&lc=US&item_name=Instagram_SSL_Pinning_Donation).  
Iranian users can donate via [IDPay](https://idpay.ir/itsmoji).  
  
Thanks.