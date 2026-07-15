Title: Last Week in Security (LWiS) - 2022-01-18
Date: 2022-01-18 19:09
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-01-18
Author: Erik
Summary: CI/CD pipeline war stories (<a href="https://twitter.com/0xZon1" target="_blank">@0xZon1</a> + others), Serv-U exploit writing (Carl Livitt of <a href="https://twitter.com/bishopfox" target="_blank">@bishopfox</a>), Safari IndexedDB leak (<a href="https://twitter.com/FingerprintJS" target="_blank">@FingerprintJS</a>), RDP services vuln (<a href="https://twitter.com/sztejnworcel" target="_blank">@sztejnworcel</a>), a very slick loader (<a href="https://twitter.com/Cerbersec" target="_blank">@cerbersec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-01-10 to 2022-01-18.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="http://www.fsb.ru/fsb/press/message/single.htm%21id%3D10439388%40fsbMessage.html" target="_blank">Illegal Activities of members of an organized criminal community stopped (REvil) [Russian, fsb.ru]</a> The FSB claims that due to recent "joint actions of the FSB and the Ministry of Internal Affairs of Russia, the organized criminal community ceased to exist, the information infrastructure used for criminal purposes was neutralized." You can even see video of the takedowns <a href="https://youtu.be/OqEWuFmzhzs" target="_blank">on YouTube</a>. While 14 individuals were arrested, it's too soon to see if this will impact REvils operations. If it does, what prompted Russia to finally take action? Google translate of the FSB releases says the "basis for the search activities was the appeal of the competent US authorities."</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21907" target="_blank">HTTP Protocol Stack Remote Code Execution Vulnerability</a>. Patch tuesday brought with it an unauthenticated RCE in Window's http.sys drivers for Windows 10 (1809+) and Server (2019+). What looks like a crash PoC is available <a href="https://github.com/nu11secur1ty/Windows10Exploits/blob/master/2022/CVE-2022-21907/PoC/PoC-CVE-2022-21907.py#L19" target="_blank">here</a>, complete with a pointless 17 second sleep.</li>
<li><a href="https://msrc-blog.microsoft.com/2022/01/11/coming-soon-new-security-update-guide-notification-system/" target="_blank">Coming Soon: New Security Update Guide Notification System</a>. Microsoft is making it easier to get notifications of changes to security update guides but the biggest news is that this system no longer requires a Live ID. A separate email/password combo can be used for the new system.</li>
<li><a href="https://fingerprintjs.com/blog/indexeddb-api-browser-vulnerability-safari-15/" target="_blank">Exploiting IndexedDB API information leaks in Safari 15</a>. "Every time a website interacts with a database, a new (empty) database with the same name is created in all other active frames, tabs, and windows within the same browser session." WebKit is slowly becoming the internet explorer of the modern browsers. PoC code <a href="https://github.com/fingerprintjs/blog-indexeddb-safari-leaks-demo" target="_blank">here</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://github.com/helpsystems/nanodump#load-nanodump-as-an-ssp" target="_blank">Load nanodump as an SSP</a>. The most advanced lsass dumper BOF was updated to allow you to load it as a Security support provider (SSP) which prevents your process from opening any handles to lsass.exe. More details on SSPs can be found <a href="https://pentestlab.blog/2019/10/21/persistence-security-support-provider/" target="_blank">here</a>.</li>
<li><a href="https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/" target="_blank">10 real-world stories of how we’ve compromised CI/CD pipelines</a>. I like the thesis here that CI/CD pipelines are just "execution engines," and without proper protection can be abused like any other system. This one is worth a read and ponder if your CI/CD pipelines would fall to any of these or similar attacks.</li>
<li><a href="https://bishopfox.com/blog/exploit-for-cve-2021-35211" target="_blank">Creating an Exploit: SolarWinds Vulnerability CVE-2021-35211</a>. This is a great walkthrough of going from CVE to shell.</li>
<li><a href="https://www.cyberark.com/resources/threat-research-blog/attacking-rdp-from-inside" target="_blank">Attacking RDP from Inside: How we abused named pipes for smart-card hijacking, unauthorized file system access to client machines and more</a>. This is incredible research and a serious vulnerability. The smart card demo was particularly impressive. This was patched last Tuesday, but should give pause to using RDP on machines with any high privileged account.</li>
<li><a href="https://hencohen10.medium.com/cyberark-endpoint-manager-local-privilege-escalation-cve-2021-44049-67cd5e62c3d2" target="_blank">CyberArk Endpoint Manager Local Privilege Escalation CVE-2021–44049.</a>. Off the high of the last article (written by a CyberArk employee), this one shows that simple permissions issues can lead to LPEs.</li>
<li><a href="https://www.varonis.com/blog/box-mfa-bypass-sms" target="_blank">Mixed Messages: Busting Box’s MFA Methods</a>. The use of a valid app-based MFA token for a controlled account allows bypass on a target account when a user only has SMS based MFA. The back end of Box must have been missing some pretty basic checks for this to work, but props for trying it!</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/01/zooming-in-on-zero-click-exploits.html" target="_blank">Zooming in on Zero-click Exploits</a>. A deep look at Zoom reveals a buffer overflow and information leak. It's not surprising that the massive code base of Zoom has issues.</li>
<li><a href="https://medium.com/@Breadman602/breadman-module-stomping-api-unhooking-using-native-apis-b10df89cc0a2" target="_blank">BreadMan Module Stomping &amp; API Unhooking Using Native APIs</a>. This new type of module stomping has some advantages, namely you don't need to load an arbitrary library into our memory space and the starting function call of the thread will point to an address space resolved usually by trusted DLLs such as ntdll.dll. Code <a href="https://github.com/Allevon412/BreadManModuleStomping" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/tothi/azure-function-proxy" target="_blank">azure-function-proxy</a> is a basic proxy as an azure function serverless app to use *[.]azurewebsites[.]net domain for phishing.</li>
<li><a href="https://github.com/Cerbersec/Ares" target="_blank">Ares</a>  is a Proof of Concept (PoC) loader written in C/C++ based on the Transacted Hollowing technique. This loader has a bunch of nice features and is far beyond the typical loader released on Github.</li>
<li><a href="https://github.com/frkngksl/ParallelNimcalls" target="_blank">ParallelNimcalls</a> is a  Nim version of MDSec's Parallel Syscall PoC. Last week it was in C++ and C#, now it's in Nim!</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/roottusk/vapi" target="_blank">vapi</a> is a Vulnerable Adversely Programmed Interface which is Self-Hostable API that mimics OWASP API Top 10 scenarios.</li>
<li><a href="https://github.com/ptswarm/reFlutter" target="_blank">reFlutter</a> is a Flutter Reverse Engineering Framework for iOS and Android apps. This framework helps with Flutter apps reverse engineering using the patched version of the Flutter library which is already compiled and ready for app repacking. This library has snapshot deserialization process modified to allow you perform dynamic analysis in a convenient way.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
