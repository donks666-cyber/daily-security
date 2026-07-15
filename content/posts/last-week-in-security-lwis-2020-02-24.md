Title: Last Week in Security (LWiS) - 2020-02-24
Date: 2020-02-24 00:40
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-02-24
Author: Erik
Summary: Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-02-17 to 2020-02-24.

<p>MITRE ATT&amp;CK techniques are in brackets after entries where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://twitter.com/hFireF0X" target="_blank">@hFireF0x</a> has been on a rampage against Windows drivers. If you are looking for a driver to add to last weeks <a href="https://github.com/hfiref0x/KDU" target="_blank">KDU</a> or <a href="https://github.com/realoriginal/dsepatch" target="_blank">dsepatch</a>, follow this user.</li>
<li><dl>
<dt><a href="https://www.vice.com/en_in/article/jgedjb/the-first-use-of-deepfakes-in-indian-election-by-bjp" target="_blank">Deepfakes are being used to spread misinformation</a>. We all knew it was coming, but this appears to be the first major use of a deepfake in an influence operation. The 2020 US election will likely see a few more. (How good are deep fakes? <a href="https://www.youtube.com/watch?v=aau8qa3xgFs" target="_blank">Really good</a>, powered by <a href="https://github.com/iperov/DeepFaceLab" target="_blank">DeepFaceLab</a>)</dt>
<dd><ul>
<li>Expect this to be used in attacks like the recent <a href="https://www.bbc.com/news/world-middle-east-51530311" target="_blank">Israeli soldiers duped Hamas fake woman ruse</a>.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.thec2matrix.com/matrix" target="_blank">The C2 Matrix</a> is out! This matrix compares the features of all the major C2 frameworks available today. This is a great resource for choosing a C2 framework, and it hope it stays updated.</li>
<li><dl>
<dt>Estonian Foreign Intelligence published its <a href="https://www.valisluureamet.ee/pdf/raport-2020-en.pdf" target="_blank">2019 annual report</a>. It contains details of Russian and Chinese operations, both military and cyber. It also has well done infographics.</dt>
<dd><ul>
<li><a href="https://threadreaderapp.com/thread/1231318658153975808.html" target="_blank">Highlights</a> by @_JakupJanda</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>Apple will enforce a maximum certificate lifetime of 398 days on certificates issues from 2020-09-01 onward. If you are using Let's Encrypt this isn't an issue. Analysis <a href="https://scotthelme.co.uk/certificate-lifetime-capped-to-1-year-from-sep-2020/" target="_blank">here</a>.</dt>
<dd><ul>
<li>Meanwhile Apple is <a href="https://www.forbes.com/sites/thomasbrewster/2020/02/22/apple-just-demanded-santander-and-a-50-billion-us-intelligence-contractor-reveal-how-they-use-iphone-hacking-tech/#289a884e46c5" target="_blank">sending subpoenas</a> to people who have tweeted about using Corellium, and <a href="https://9to5mac.com/2020/02/19/app-store-confidential/" target="_blank">attempting to block the publication</a> of a book written by former App Store manager Tom Sadowski, "App Store Confidential."</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://twitter.com/underthebreach/status/1231150591474356225" target="_blank">Chinese Bitcoin investor loses 45MM USD in sim swapping attack</a>. If you have more money in cryptocurrency than you would carry in your wallet, it's time to buy and use hardware wallet. Same rule applies for how much cryptocurrency you should keep on an exchange.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://twitter.com/danusminimus" target="_blank">@danusminimus</a> dropped the <a href="https://danusminimus.github.io/Analyzing-Modern-Malware-Techniques-Part-4/" target="_blank">4th part</a> of his very through "Analyzing Modern Malware Techniques" blog. If you are interested in deeply technical malware reversing, this is a great read.</li>
<li><a href="www.38sierra.com/posts/20200211/">MacOS Instrumentation for Insider Threats</a> walks through using the basic security module of macOS to audit file access and potentially detect unusual file access patterns for post-compromise or insider threat detection. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1005/" target="_blank">T1005 Data from Local System</a>]</li>
<li><dl>
<dt><a href="https://medium.com/tenable-techblog/bypass-windows-10-user-group-policy-and-more-with-this-one-weird-trick-552d4bc5cc1b" target="_blank">Bypass Windows 10 User Group Policy (and more) with this One Weird Trick</a> - Clickbait title aside, this is a great find on how unprivileged users can bypass group policy, and even gain code execution or bypass AV. I won't be surprised when ransomware uses this to disable "protected" AV via the registry on reboot and then starts encrypting files. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1112/" target="_blank">T1112 Modify Registry</a>]</dt>
<dd><ul>
<li>Detection: Detect a write of a "ntuser.man" file in a userprofile directory.</li>
<li>Sysmon rule: <cite>&lt;TargetFilename condition="end with"&gt;ntuser.man&lt;/TargetFilename&gt; &lt;!--Group Policy bypass--&gt;</cite></li>
</ul>
</dd>
</dl>
</li>
<li>Casey Smith (<a href="https://twitter.com/subTee" target="_blank">@subTee</a>) demoed the ability to <a href="https://twitter.com/subTee/status/1230345137173098497/photo/1" target="_blank">highjack arbitrary .Net assemblies</a> using a runtime configuration and the <a href="https://docs.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/runtime/probing-element" target="_blank">probing</a> functionality. This should be researched for its potential as a persistence technique and AV bypass.</li>
<li><a href="https://www.mdsec.co.uk/2020/02/getting-what-youre-entitled-to-a-journey-in-to-macos-stored-credentials/" target="_blank">Getting What You’re Entitled To: A Journey Into MacOS Stored Credentials</a> has two good examples of post exploitation credential harvesting from applications (Microsoft Remote Desktop and Google Drive Backup and Sync) even when an application is protected by the "Hardened Runtime." [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1003/" target="_blank">T1003 Credential Dumping</a>]</li>
<li><a href="https://medium.com/@__rishabh__/open-redirect-to-account-takeover-e939006a9f24" target="_blank">Open redirect to account takeover</a> is a short writeup on how to convert an open redirect vulnerability to cookie stealing.</li>
<li><a href="https://khast3x.club/posts/2020-02-14-Intro-Modern-Routing-Traefik-Metasploit-Docker/" target="_blank">Introduction To Modern Routing For Red Team Infrastructure - using Traefik, Metasploit, Covenant and Docker</a> does what it says on the tin. The sometimes tricky traefik 2.0 rules-as-labels setup is explained in detail for Metasploit and Covenant.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/BishopFox/GadgetProbe" target="_blank">GadetProbe</a> is a Burp Extension from BishopFox that can aid in identifying remote Java Classpaths even with blind deserialization. Their <a href="https://know.bishopfox.com/research/gadgetprobe" target="_blank">writeup</a> is worth a read. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/FSecureLABS/physmem2profit" target="_blank">phsmem2profit</a> is a tool from F-Secure that uses the winpmem driver to remotely access a Windows target's memory and extract credentials. Their <a href="https://labs.f-secure.com/blog/rethinking-credential-theft" target="_blank">blog post</a> has the details. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1003/" target="_blank">T1003 Credential Dumping</a>]</li>
<li><a href="https://www.mdsec.co.uk/2020/02/cve-2020-0618-rce-in-sql-server-reporting-services-ssrs/" target="_blank">CVE-2020-0618: RCE in SQL Server Reporting Services (SSRS)</a> exploits a deserialization issue and allows anyone authorized to view the SSRS to achieve remote code execution as <cite>nt servicereportserver</cite>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/nyxgeek/onedrive_user_enum" target="_blank">onedrive_user_enum</a> allows the enumeration of Office365 domain users that have logged into OneDrive in the past. This provides a reliable enumeration method that is unmonitored and replaces the <a href="https://grimhacker.com/2017/07/24/office365-activesync-username-enumeration/" target="_blank">patched ActiveSync enumeration</a> technique. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1078/" target="_blank">T1078 Valid Accounts</a>]</li>
<li><a href="https://github.com/djhohnstein/KittyLitter" target="_blank">KittyLitter</a> is a credential dumper service for Windows that binds to TCP, SMB, and MailSlot channels to communicate credential material to the lowest privilege attackers. This is likely not that useful for offensive engagements, but would be a great tool for attack and defend CTFs where a defender may be rolling creds and trying to kick you off a box. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1003/" target="_blank">T1003 Credential Dumping</a>]</li>
<li><a href="https://github.com/rasta-mouse/GadgetToJScript" target="_blank">GadgetToJScript</a>, rasta-mouse fork, makes GadgetToJSscript more user friendly by allowing input files and reference assemblies on the command line instead of hardcoding them which required recompiling the tool. Rastamouse has a <a href="https://rastamouse.me/2020/02/gadgettojscript/" target="_blank">blog post</a> that details the changes as well. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1064/" target="_blank">T1064 Scripting</a>]</li>
<li><a href="https://github.com/0x09AL/IIS-Raid" target="_blank">IIS-Raid</a> is a native IIS module that abuses the extendibility of IIS to backdoor the web server and carry out custom actions defined by an attacker by 0x09AL of MDSec. The <a href="https://www.mdsec.co.uk/2020/02/iis-raid-backdooring-iis-using-native-modules/" target="_blank">MDSec blog</a> has details. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1100/" target="_blank">T1100 Web Shell</a>]</li>
<li><a href="https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi" target="_blank">CVE-2020-1938 Apache Tomcat AJP file read PoC</a>. Deserialization strikes again. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/monoxgas/Koppeling" target="_blank">Koppeling</a> by Silent Break Security enables advanced DLL Hijacking (maintain stability of the source process, keep code execution within the process, and get around complexities involved in loader lock). Their <a href="https://silentbreaksecurity.com/adaptive-dll-hijacking/" target="_blank">blog post</a> has all the details. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1038/" target="_blank">T1038 DLL Search Order Hijacking</a>]</li>
<li><dl>
<dt><a href="https://github.com/JustasMasiulis/inline_syscall" target="_blank">inline_syscall</a> is another header for C++ project on windows that allows for easy inlining of syscalls on windows. This project requires the use of clang, but does highly optimize and inline the direct syscalls. The first EDR to develop a generic detection for direct syscalls will likely have some unique detections. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0005/" target="_blank">TA0005 Defense Evasion</a>]</dt>
<dd><ul>
<li>This joins <a href="https://github.com/jthuraisamy/SysWhispers" target="_blank">SysWhispers</a>, a less optimized but more user friendly library for direct system calls.</li>
<li><a href="https://twitter.com/Cneelis" target="_blank">@Cneelis</a>'s <a href="https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/" target="_blank">blog post</a> which introduced the concept of direct syscalls.</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt><a href="https://github.com/mhaskar/CVE-2020-8813" target="_blank">CVE-2020-8813</a> is simple exploit for a pre (if a guest has real time graph privilege - not default) and post authentication command injection vulnerability in the Cacti network monitoring web frontend. This is a 90's/early 2000's style command injection in a cookie; legacy software with legacy bugs. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</dt>
<dd><ul>
<li>Only affects PHP &lt; 7.2 and Cacti &lt; 1.2.10 (not released as of 2020-02-24; 0day)</li>
<li><a href="https://drive.google.com/file/d/1A8hxTyk_NgSp04zPX-23nPbsSDeyDFio/view" target="_blank">Demo</a></li>
<li><a href="https://github.com/Cacti/cacti/commit/fea919e8fe05bb730c802054661fd3a7ec029784" target="_blank">Patch</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/med0x2e/NoAmci" target="_blank">NoAmci</a> uses DInvoke (from the SharpSploit update last week) to patch AMSI.dll in order to bypass AMSI detections triggered when loading .NET tradecraft via Assembly.Load(). As the offensive community moves from PowerShell to .Net EDR has started to catch up and these types of bypasses are required against advanced EDR. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1054/" target="_blank">T1054 Indicator Blocking</a>]</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/blendin/3snake" target="_blank">3snake</a> is a tool for extracting information from newly spawned processes on Linux. This could easily be weaponized to ship creds back to a C2 once a box is rooted.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
