# Instagram SSL Pinning
Bypass Instagram SSL Pinning on Android (`x86`) Version **83.0.0.20.111** (ARM Coming soon)

Requirements
------------
* Instagram **x86** APK ([Download](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-instagram-83-0-0-20-111-144612-release/instagram-83-0-0-20-111-4-android-apk-download/))  

* a **rooted x86** android device (Physical or virtual)  
   *[Genymotion](https://www.genymotion.com/) Android 7+ suggested.*  
   *Genymotion virtual devices is rooted by default.*
   
* ADB ([Download](https://developer.android.com/studio/releases/platform-tools.html))  
    *Genymotion will install ADB automatically and you can find it on `<Installation path>/tools`*
  
* Latest version of JDK ([Download](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html))

* Burp Suite (***.Jar version**) ([Download](https://portswigger.net/burp/communitydownload))

Usage
-----
1. Install Genymotion, your virtual device and start it.  

2. Download and install Instagram apk on your device.  

3. Run Instagram and close it.  
  ***It's important to run Instagram app once before patching!***  
  
4. Download the patched file ([x86](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/x86)) and push it to the device:  
  `adb push libliger.so /data/data/com.instagram.android/lib-zstd/libliger.so`  
  
5. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your android device.  

6. That's it! Now open the Instagram app on your device and intercept the requests in Burp Suite !

Instagram Signature Key (v 83.0.0.20.111) ARM and x86
-------------------------------------------
`63f299bfd017344effa1523d46f288bacaa7fcc5f5bdd3c735318ebb35a46ff8`

Donations
--------
If you want to show your appreciation, you can donate via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=its13moji%40gmail%2ecom&lc=US&item_name=Instagram_SSL_Pinning_Donation). Thanks!