# Instagram SSL Pinning
Bypass Instagram SSL Pinning on Android (`ARM, x86 and AArch64`) Version **237.0.0.14.102** 

**Do you like this project? Support it by donating**

- **Bitcoin**: bc1qfr59gu23rxurhj8aarerx3y6gmh546kf88cte6
- **Ethereum**: 0xbCdC08E42B31ECB9a97749F69BCce7AcE6834cAC
- **Dogecoin**: DEvEGbjmKw8v2Rka9JbKVWMBepXfZh95Zf  

- [![Buy me a coffee][buymeacoffee-shield]][buymeacoffee]

[buymeacoffee]: https://www.buymeacoffee.com/itsmoji
[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png

### **About ARM Patched APK (Non-Root Method)**
In recent versions, Instagram added a new encryption layer (or maybe just a custom compression method) to the ARM libraries that need to be decrypted to create the patched APK. Currently, I'm busy with my projects and don't have time to work on it. I've added an encrypted file to the [dev/](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/dev) folder; you can download and take a look at it. If you know what this file is and how it can be decrypted/decompressed, please contact me or open a new issue.

## Requirements

* The latest version of JDK ([Download](https://www.oracle.com/java/technologies/javase-jdk15-downloads.html))

* The latest version of ([Burp Suite](https://portswigger.net/burp/releases/community/latest)) or ([mitmproxy](https://mitmproxy.org/))  
  
* Instagram APK ([ARM](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-instagram-237-0-0-14-102-release/instagram-237-0-0-14-102-7-android-apk-download/) - [x86](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-instagram-237-0-0-14-102-release/instagram-237-0-0-14-102-13-android-apk-download/) - [AArch64](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-instagram-237-0-0-14-102-release/instagram-237-0-0-14-102-2-android-apk-download/)) - ***For root method only***  
  ***Download only from these links, not Google Play or somewhere else***  
  
* a **rooted** Android device (Physical or virtual) - ***For root method only***  
   *[Genymotion](https://www.genymotion.com/) Android 8+ recommended.*  
   *Genymotion virtual devices is x86 and rooted by default.*  
   
* ADB ([Download](https://developer.android.com/studio/releases/platform-tools.html)) - ***For root method only***  
    *Genymotion will install ADB automatically, and you can find it on `<Genymotion Installation path>/tools`*
  
## Non-Root Method (Recommended)

### Instructions

1. Download and install patched APK ([ARM](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/non-root/arm) - [x86](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/non-root/x86))  
    ***ARM on a physical device or ARM on Genymotion Android 8-Oreo with [ARM Translation](https://mega.nz/#F!JhcFwKpC!yfhfeUzvIZoSdBgfdZ9Ygg) strongly recommended!***

    1.2. **For x86 only,** Open Instagram app (wait a few seconds) and close it.  
           ***It's important to run Instagram app once, before setting the proxy!***  

2. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your Android device.  
    *Don't forget to **turn off** the Burp proxy intercept from `Proxy > Intercept` tab*  
    *You should [install Burp Suite certificate on your Android device](https://distributedcompute.com/2017/12/12/tech-note-installing-burp-certificate-on-android/)* 

3. That's it! Now open the Instagram app on your device and intercept the requests in Burp Suite !  

## Root Method

[Watch tutorial video](https://youtu.be/gmYzlpy2Ii4) 

### Instructions (**It's important to do step by step**) 

1. Download and install Instagram apk on your device.  

2. Open Instagram app (wait a few seconds) and close it.  
  ***It's important to run Instagram app once, before start patching!***  
  
3. Download the patched file ([ARM](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/arm) - [x86](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/x86) - [AArch64](https://github.com/itsMoji/Instagram_SSL_Pinning/tree/master/arm64-v8a)) and push it to the device:  
  ARM, x86 and AArch64: `adb push libliger.so /data/data/com.instagram.android/lib-compressed/libliger.so`  
  
4. Open Instagram app again (wait a few seconds) and close it.  
  
5. Run Burp Suite with `/<JDK Installation path>/bin/java -jar burpsuite_community.jar` and setting up proxy on your Android device.  
    ***You must set the proxy in this step***  
    *Don't forget to **turn off** the Burp proxy intercept from `Proxy > Intercept` tab*  
    *You should [install Burp Suite certificate on your Android device](https://distributedcompute.com/2017/12/12/tech-note-installing-burp-certificate-on-android/)* 
    
6. That's it! Now open the Instagram app and intercept the requests in Burp Suite !

## Instagram Signature Key for ARM and x86

* **v136.0.0.34.124:** `46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b`  
* Instagram does not sign requests in versions newer than 136.0.0.34.124, it's just `SIGNATURE` string.  
    Example: `signed_body=SIGNATURE.{"phone_id":"51df5a24-e59e-46cd-bc01-fe658aba9f18","_csrftoken":"mPzWvJ399rqCxOY5rn6Bggq7oOcFkf6U","usage":"prefill"}`
