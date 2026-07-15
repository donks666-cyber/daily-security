Title: Last Week in Security (LWiS) - 2020-02-17
Date: 2020-02-17 11:40
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-02-17
Author: Erik
Summary: Last Week in Security (LWiS) is a summary of the interesting cyber security news, techniques, tools and exploits from the previous week. This post covers 2020-02-10 to 2020-02-17.

<p>Now with MITRE ATT&amp;CK techniques in brackets where appropriate!</p>
<section id="news">
<h2>News</h2>
<ul>
<li>The US Attorney General <a href="https://apnews.com/05aa58325be0a85d44c637bd891e668f" target="_blank">indicted four suspected Chinese PLA members</a> for the Equifax breach in 2017. The indictment states that the attackers wiped log files daily and routed traffic through dozens of servers in nearly 20 countries. Of note, one photo appears to be from a laptop camera, which indicates a possible "hack back" operation or potentially prior access by US intelligence.</li>
<li>CIA and BND (German CIA+NSA) <a href="https://arstechnica.com/tech-policy/2020/02/us-german-intel-owned-swiss-crypto-used-by-dozens-of-countries/" target="_blank">owned and subverted the Swiss cryptography company Crypto AG</a> from 1970 to 2018. Supply chain risk just got another poster child. Alex Stamos (former Yahoo/Facebook security exec) shared the time a Hardware Security Module (HSM) was... <a href="https://twitter.com/alexstamos/status/1227336985972314112" target="_blank">tampered with</a> prior to delivery. Still not scared of <a href="https://www.wsj.com/articles/u-s-officials-say-huawei-can-covertly-access-telecom-networks-11581452256" target="_blank">Huawei</a>? <a href="https://arstechnica.com/tech-policy/2020/02/us-gave-allies-evidence-that-huawei-can-snoop-on-phone-networks-wsj-says/" target="_blank">Hmm</a>? [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1195/" target="_blank">T1195</a>]</li>
<li><a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>, the AD whisperer, revealed that <a href="https://twitter.com/_dirkjan/status/1227308294676664320" target="_blank">CVE-2020-0665 was patched on Tuesday</a> and is able to use "kerberos magic" to bypass forest security boundaries. More to come in April. Note this is unrelated to @harmj0y's <a href="https://www.harmj0y.net/blog/redteaming/not-a-security-boundary-breaking-forest-trusts/" target="_blank">forest trust research</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0008/" target="_blank">TA0008</a>]</li>
<li><dl>
<dt>Security Key News</dt>
<dd><ul>
<li>Google open sources titan security key firmware as <a href="https://github.com/google/OpenSK" target="_blank">OpenSK</a>, a rust application for <a href="https://www.tockos.org/" target="_blank">Tock OS</a> running on a <a href="https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle" target="_blank">Nordic nRF52840</a> dongle.</li>
<li><a href="https://github.com/snopf/snopf" target="_blank">snopf</a> is a new open source USB "password tool" that works differently than a Yubikey or Google's Titan. It generates a password from a master seed based on parameters passed to it and emulates a keyboard to input the password when a physical button is pressed.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://twitter.com/Fox0x01/" target="_blank">@Fox0x01</a> is back at it! <a href="https://azeria-labs.com/trusted-execution-environments-tee-and-trustzone/" target="_blank">Understanding trusted execution environments and ARM TrustZone</a> is a great resource on how Trusted Execution Environments work on modern Android phones and their attack surface.</li>
<li>The Joshua Schulte trial (accused leaker of CIA tools "Vault 7") is underway and already contains some OPSEC fails. It <a href="https://twitter.com/emptywheel/status/1228458401522487298" target="_blank">appears</a> Joshua downloaded TAILS and searched for disk wiping and MD5 sum utilities right after a USB was delivered from Amazon. Multiple levels of fail here, but if you buy a book on hiding bodies the day your spouse goes missing, the jury doesn't need to see the body to think you did it... [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1488/" target="_blank">T1488</a>]</li>
<li><a href="https://unc0ver.dev/" target="_blank">unc0ver 4.0.1</a> is out, with support for iOS 13.1-13.3 on A12 and A13 (iPhone XS series, 11, and 11 Pro). This is the first time these devices have been supported by a jailbreak tool as checkra1n only supports i-devices up to the iPhone X. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068</a>]</li>
<li><a href="https://imagemonkey.io/" target="_blank">ImageMonkey</a>, an open source repository of classified and tagged images, just surpassed 100,000 images. It is all available for free and even has an API. If you are doing any ML classification training involving images (or just learning ML and need data sets) this is a great resource.</li>
<li>US Cert has <a href="https://www.us-cert.gov/ncas/analysis-reports" target="_blank">released 7 new detailed malware reports on DPRK malware</a>, as well as releasing samples via Virus Total. These reports include code snippets on decoding C2 traffic and yara rules in addition to standard IOCs.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><dl>
<dt>Ruben Boonen (<a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a>) and The Wover (<a href="https://twitter.com/TheRealWover" target="_blank">@TheRealWover</a>) released their BlueHatIL 2020 talk: Staying # and Bringing Covert Injection Tradecraft to .NET. This talk covers why C# is the natural successor to Powershell in today's offensive security environment. This talk covers a new API for code injection they have an open Pull request to <a href="https://github.com/cobbr/SharpSploit/pull/43" target="_blank">SharpSploit</a>. I am excited to develop against this and see others do the same! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1055/" target="_blank">T1055</a>]</dt>
<dd><ul>
<li><a href="https://github.com/FuzzySecurity/BlueHatIL-2020/blob/master/Ruben%20Boonen%20%26%20TheWover%20-%20BHIL2020_Staying%23_v0.4.pdf" target="_blank">Slides</a></li>
<li><a href="https://www.youtube.com/watch?v=FuxpMXTgV9s" target="_blank">Video</a></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>Netgear put their TLS private key in some router firmware images so they could dynamically sign routerlogin.net. This opens up some fun potential attacks if you own DNS or a gateway.</dt>
<dd><ul>
<li><a href="https://gist.github.com/nstarke/a611a19aab433555e91c656fe1f030a9" target="_blank">Original finding</a></li>
<li><a href="https://saleemrashid.com/2020/02/09/exploiting-netgear-routerlogin/" target="_blank">Blog Post</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.praetorian.com/blog/running-a-net-assembly-in-memory-with-meterpreter" target="_blank">In memory execution of .NET with meterpreter</a> by Thomas Hendrickson of Praetorian [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1086/" target="_blank">T1086</a>]</li>
<li>Hexacorn is <a href="http://www.hexacorn.com/blog/2020/02/13/run-lola-bin-run/" target="_blank">at it again</a>, this time loading COM objects with rundll32.exe's <cite>-localserver</cite> argument. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1175/" target="_blank">T1175</a>]</li>
<li><a href="https://www.blackarrow.net/mssqlproxy-pivoting-clr/" target="_blank">Lateral movement via MSSQL: a tale of CLR and socket reuse</a> is a great write up of how a red team developed a custom tool to reuse a MSSQL socket to implement a socks5 proxy and hit servers behind the DMZ that were accessible to the MSSQL server. <a href="https://github.com/blackarrowsec/mssqlproxy" target="_blank">mssqlproxy</a>  available on github. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0008/" target="_blank">TA0008</a>]</li>
<li><a href="https://research.nccgroup.com/2020/02/12/command-and-kubectl-talk-follow-up/" target="_blank">Deep Dive into Real-World Kubernetes Threats</a> presents techniques for attacking Kubernetes pods. Next time you see k8s on an engagement, this may be a good starting point. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190</a>]</li>
<li><a href="https://about.gitlab.com/blog/2020/02/12/plundering-gcp-escalating-privileges-in-google-cloud-platform/" target="_blank">Tutorial on privilege escalation and post exploitation tactics in Google Cloud Platform environments</a> presents an overview and common issues with GGP and how they can be exploited, including lateral movement.</li>
<li>NTT Group released a <a href="https://github.com/malrev/ABD" target="_blank">great course on practical malware deobfuscation</a>. This course goes through obfuscation principles, the theory and practice of obfuscated code analysis, and even data-flow analysis and SAT/SMT-based binary analysis. This is high quality training quality material, thanks NTT Group! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1140/" target="_blank">T1140</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><p>VirusTotal releases an <a href="https://blog.virustotal.com/2020/02/official-virustotal-plugin-for-ida-pro-7.html" target="_blank">official Plugin</a> for IDA Pro 7. It enables you to search for bytes, strings, similar code, or similar functions against the worlds largest collection of binaries to help your analysis. Standard VT licenses allow 90 days retrospection and Threat Hunter PRO allows for 1 year retrospection. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1140/" target="_blank">T1140</a>]</p>
</li>
<li><p>Hashcat can now <a href="https://twitter.com/hashcat/status/1129441728761610242" target="_blank">crack zip files using PKZIP</a> at an insane rate of 22.7 ZettaHash/s on a single 2080Ti. Any PKZIP password shorter than 20 characters is not safe.</p>
</li>
<li><dl>
<dt>Bloodhound 3.0 released! <a href="https://docs.google.com/presentation/d/1vZ1QckmtjpBsOff85IaP1mt4fEDmWYW3ziAHVHiLd5I/" target="_blank">Slides and Demos</a> are available, as is a companion <a href="https://posts.specterops.io/introducing-bloodhound-3-0-c00e77ff0aa6" target="_blank">blog</a>. Updates below. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1482/" target="_blank">T1482</a>]</dt>
<dd><ul>
<li>Powershell Remoting (port 5985/5986).</li>
<li><dl>
<dt>Control of Group Managed Service Account. Allows reading of plaintext password remotely by authorized principles</dt>
<dd><ul>
<li><a href="https://github.com/rvazarkar/GMSAPasswordReader" target="_blank">GMSAPasswordReader</a></li>
<li>Defenders audit DC permission with BloodHound and look for event ID 2947 in the Direct Service log to detect this technique</li>
</ul>
</dd>
</dl>
</li>
<li>SID History - This is the property used for Golden Ticket attacks, now visible in BloodHound 3.0</li>
<li>OU Control - Adds the ability to push ACEs to OUs</li>
<li>SharpHound total rewrite (based on .NET 4.5) that gives ~30% faster LDAP collection (600k computers in a few hours!), better caching, and more accurate data collection</li>
<li>Various quality of life improvements: large graph drawing warning, improved dark mode, improved node data display, etc</li>
<li>During the webinar, the BloodHound team mentioned <a href="https://hausec.com/2019/09/09/bloodhound-cypher-cheatsheet/" target="_blank">this great BloodHound Cypher cheatsheet</a> for common queries</li>
<li>Best detection is to find "loud LDAP talkers" because the collection of lots of LDAP data is a primitive that cannot be changed for BloodHound to work</li>
</ul>
</dd>
</dl>
</li>
<li><p>Mimikatz was updated last week to dump creds from Chrome, and it also <a href="https://twitter.com/gentilkiwi/status/1227379141902786561" target="_blank">works with the new Edge beta</a> (Chromium based). [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1503/" target="_blank">T1503</a>]</p>
</li>
<li><p>Windows Local Privilege Elevation Exploits. Is anyone <em>not</em> SYSTEM at this point? It seems like a new LPE is dropped every day! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068</a>]</p>
<blockquote>
<ul>
<li><dl>
<dt>CVE-2020-0683 - Windows MSI “Installer service” Elevation of Privilege. This was patched on tuesday, but (surprise) another symbolic link handling bug, this time within MSI packages being installed, allowed an unprivileged attacker to write to arbitrary files. Like all LPEs this requires code to already be executing on the target, but looks like a nice solid LPE for the new year.</dt>
<dd><ul>
<li><a href="https://itm4n.github.io/cve-2020-0668-windows-service-tracing-eop/" target="_blank">itm4n's writeup</a></li>
<li><a href="https://github.com/padovah4ck/CVE-2020-0683" target="_blank">PoC</a></li>
<li>Weaponization: implement the PoC in C# and run a DLL with <a href="https://github.com/itm4n/UsoDllLoader" target="_blank">UsoDllLoader</a>, then clean up.</li>
<li>Generic Detection: Alert on file creation or symlinking of C:\windows\system32\WindowsCoreDeviceInfo.dll</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>Local Privilege Escalation in many Ricoh Printer Drivers for Windows (CVE-2019-19363) disclosed by pentagrid. If you are on a windows box, look for anything with PCL6 in the driver name and you can likely get SYSTEM.</dt>
<dd><ul>
<li><a href="https://www.pentagrid.ch/en/blog/local-privilege-escalation-in-ricoh-printer-drivers-for-windows-cve-2019-19363/" target="_blank">Writeup and PoC</a></li>
<li><a href="https://www.ricoh.com/info/2020/0122_1/list" target="_blank">List of affected drivers</a></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>AMD User Experience Program Launcher from Radeon Software is vulnerable to an insecure file move which leads to LPE</dt>
<dd><ul>
<li><a href="https://heynowyouseeme.blogspot.com/2020/02/privilege-escalation-filewrite-eop-in.html" target="_blank">Writeup</a></li>
<li><a href="https://github.com/sailay1996/amd_eop_poc" target="_blank">PoC (amd_eop_poc)</a></li>
<li>Vulnerable Versions: AUEPLauncher (&lt;= 1.0.0.1), AUEPMaster (&lt;= 1950.15.1.117)</li>
<li>Weaponization: Same as CVE-2020-0683, C# version that can be run in memory and only drop the WindowsCoreDeviceInfo.dll to disk</li>
<li>Generic Detection: Alert on file creation or symlinking of C:\windows\system32\WindowsCoreDeviceInfo.dll</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/itm4n/PrivescCheck" target="_blank">PrivescCheck</a> is a fresh PowerShell v2 script that aims to be a dependency free yet feature filled Windows privesc checker.</li>
</ul>
</blockquote>
</li>
<li><p>Inspired by <a href="https://blog.orange.tw/2019/07/attacking-ssl-vpn-part-1-preauth-rce-on-palo-alto.html" target="_blank">Orange Tsai's SSL VPN research</a>, <a href="https://twitter.com/plopz0r" target="_blank">@plopz0r</a> found <a href="https://blog.scrt.ch/2020/02/11/sonicwall-sra-and-sma-vulnerabilties/" target="_blank">6 (!) vulnerabilities</a> in SonicWall devices, including 3 pre-auth (SQLi for authenticated sessions, a classic buffer overflow, and a path traversal [existence only]). Patch your SonicWalls! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1133/" target="_blank">T1133</a>]</p>
</li>
<li><dl>
<dt><a href="https://github.com/hfiref0x/KDU" target="_blank">KDU</a> is a seriously impressive project that abstracts away the hard part of getting kernel execution on windows by leveraging vulnerable drivers that are compiled into a single executable. It works on everything from Windows 7 to Windows 10 20H2, even with SecureBoot enabled. It wouldn't be hard to take this project and weaponize it, especially if you have a driver 0day on your hands. Top marks to hfiref0x. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068</a>]</dt>
<dd><ul>
<li>This joins <a href="https://github.com/realoriginal/dsepatch" target="_blank">dsepatch</a>, another driver signing enforcement cradle and <a href="https://github.com/alxbrn/gdrv-loader" target="_blank">gdrv-loader</a> from last week, but dsepatch requires you provide your own vulnerable driver.</li>
</ul>
</dd>
</dl>
</li>
<li><p><a href="https://github.com/karalabe/xgo" target="_blank">xgo</a>: Cross compiling Go (golang) is easy in theory, but as soon as you start extending Go with C-based languages or modules, things get complicated. xgo makes building a go project for all targets as easy as <cite>xgo github.com/[user]/[go-project]</cite>.</p>
</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/nshalabi/SysmonTools" target="_blank">SysmonTools</a> is a powerful collection of tools for investigating Sysmon and pcap logs.</li>
<li>Go (golang) is a great language for a number of reasons, but one drawback can be binary size. <a href="https://github.com/jondot/goweight" target="_blank">goweight</a> is a tool that shows you what is taking up space in your compiled golang binaries, which allows you to make informed choices about dependancies.</li>
<li><a href="https://github.com/lirantal/npq" target="_blank">npq</a> npq is a drop in replacement for npm that adds a bunch of safety and vulnerability checks. It won't save you from someone cleverly backdooring a package, but it will at least check for known vulns and metrics like age and number of downloads. A baby step forward for the dumpster fire that is javascript dependency management. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1195/" target="_blank">T1195</a>]</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
