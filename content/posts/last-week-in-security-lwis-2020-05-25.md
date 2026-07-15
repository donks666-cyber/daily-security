Title: Last Week in Security (LWiS) - 2020-05-25
Date: 2020-05-25 20:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-05-25
Author: Erik
Summary: iOS 0day, privacy news, a patch diffing exploit from <a href="https://twitter.com/matteomalvica" target="_blank">@matteomalvica</a>, <a href="https://twitter.com/404death" target="_blank">@404death</a> drops a powerful Windows LPE primitive, <a href="https://twitter.com/BillDemirkapi" target="_blank">@BillDemirkapi</a> manages to execute shellcode in the kernel with Trend Micro's RootKit Remover, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-05-18 to 2020-05-25.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><dl>
<dt>Privacy News</dt>
<dd><ul>
<li><a href="https://nullsweep.com/why-is-this-website-port-scanning-me/" target="_blank">Why is This Website Port Scanning me?</a> Websockets are being used for "anti-fraud" scans of website user's local machines. The theory is that if a user is running a VNC or other remove desktop server, they may be part of a botnet/click farm operation I suppose. If you are a developer this could be <a href="https://medium.com/@stestagg/stealing-secrets-from-developers-using-websockets-254f98d577a0" target="_blank">especially dangerous</a>. In Firefox, setting <cite>network.websocket.max-connections</cite> to 0 will disable websockets, but lots of modern web applications rely on them.</li>
<li><a href="https://medium.com/tenable-techblog/turning-signal-app-into-a-coarse-tracking-device-643eb4298447" target="_blank">Abusing WebRTC to Reveal Coarse Location Data in Signal</a> abused WebRTC on both iOS and Android in order to reveal the user's <a href="https://developers.google.com/speed/public-dns/docs/ecs" target="_blank">ENDS</a> client subnet, which could reveal a rough location (~400 mile radius). The bug has been patched in the latest version of Signal.</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>macOS 10.15 Catalina notarization news</dt>
<dd><ul>
<li><a href="https://lapcatsoftware.com/articles/catalina-executables.html" target="_blank">Catalina is checking notarization of unsigned executables</a> started the firestorm, bringing to light that macOS sends the hash of every executable not whitelisted in System Preferences as a "Developer Tool" to Apple.</li>
<li><a href="https://medium.com/sensorfu/how-my-application-ran-away-and-called-home-from-redmond-de7af081100d" target="_blank">How my application ran away and called home from Redmond</a> is an example of arguably more invasive behavior on Windows. Additionally, "SmartScreen" also profiles and reports "usual" executions to Microsoft.</li>
<li>This effectively gives Apple a list of binaries being run by every user, without a way to disable it (besides going fully offline).</li>
<li><a href="https://www.wired.com/story/inside-the-nsas-secret-tool-for-mapping-your-social-network/" target="_blank">Inside the NSA’s Secret Tool for Mapping Your Social Network</a> shows the power of massive metadata collection, and its ability for misuse. Perhaps tomorrow Apple receives a request for all users that have run the Tor browser in your country.</li>
<li>A happy medium would be to push a bloom filter of known hashes to end users and perform local lookups, only sending hashes that don't hit the bloom filter to Apple for further analysis. This is what Google Chrome does for phishing site lookups (until Enhanced Safe Browsing Protection is enabled). Users should also be given the ability to opt out of such features.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="http://www.nxnsattack.com/" target="_blank">New DNS Vulnerability Lets Attackers Launch Large-Scale DDoS Attacks</a> With up to 1000x traffic amplification, this will likely see exploitation soon. If you are responsible for DNS severs, patch them quickly.</li>
<li><a href="https://about.gitlab.com/releases/2020/05/22/gitlab-13-0-released/" target="_blank">GitLab 13.0</a> released with many new changes. The biggest for most users will likely be the new "Deploy to Amazon ECS" that makes AWS a first class citizen for deployments and monitoring on par with previously supported Google Cloud.</li>
<li><a href="https://security.googleblog.com/2020/05/enhanced-safe-browsing-protection-now.html" target="_blank">Enhanced Safe Browsing Protection now available in Chrome</a> will check uncommon URLs in real time. Phishing against Chrome users just got harder.</li>
<li><a href="https://unc0ver.dev/" target="_blank">Jailbreak for iOS 11.0-13.5 for all iOS devices released</a>. After a few tough iOS releases, the jailbreaking scene is back in full force. First <a href="https://checkra.in/" target="_blank">checkra1n</a>, and now a fast, reliable jailbreak for every iOS device on the latest, signed version. Hats off to the hackers that have kept pushing Apple despite new security additions to iOS (i.e. <a href="https://events.static.linuxfound.org/sites/events/files/slides/slides_23.pdf" target="_blank">Pointer Authentication</a>). Why release this 0day now? Perhaps the <a href="https://www.vice.com/en_us/article/5dzpxz/how-iphone-hackers-got-hands-on-new-ios-14-months-before-realease" target="_blank">iOS 14 leak</a> gave the jailbreak developers enough insight to see that it was patched. Add <a href="https://frida.re/docs/ios/" target="_blank">build.frida.re</a> to your cydia repo list and start hacking those iOS apps! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.matteomalvica.com/blog/2020/05/21/lpe-path-traversal/" target="_blank">Distrusting the patch: a run through my first LPE 0-day, from command injection to path traversal</a>. Great writeup from <a href="https://twitter.com/matteomalvica" target="_blank">@matteomalvica</a> showing the powerful technique of patch diffing to determine if patches address the root issues or only stop one known variant. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/windows-10-quietly-got-a-built-in-network-sniffer-how-to-use/" target="_blank">Windows 10 quietly got a built-in network sniffer</a>. The Windows 10 October 2018 Update included pktmon.exe. In the 10 May (build 2004) update, it includes live packet output and the ability to convert to pcapng format. If that isn't available, Microsoft's <a href="https://www.microsoft.com/en-in/download/details.aspx?id=4865" target="_blank">Windows Network Monitor</a> can be used to view the ETL file that is generated. It's disappointing but not unexpected for Microsoft to use their own syntax for filters instead of the industry standard BPF.</li>
<li><a href="https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/" target="_blank">Ragnar Locker ransomware deploys virtual machine to dodge security</a>. To avoid endpoint protection, Ragnar ships a copy of Sun xVM VirtualBox from 2009 and a stripped-down version of the Windows XP SP3 (MicroXP v0.82). This virtual machine is booted and all local disks, connected removable drives, and mapped network drives on the physical machine are mapped into the VM where the actual Ragnar ransomware runs and encrypts the files. As someone who glues tools together to achieve operational objectives, I have to respect the creative problem solving demonstrated here. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</li>
<li><a href="https://billdemirkapi.me/How-to-use-Trend-Micro-Rootkit-Remover-to-Install-a-Rootkit/" target="_blank">How to use Trend Micro's Rootkit Remover to Install a Rootkit</a>. So much goes wrong with Trend Micro's Rootkit Remover its worth reading the full article. The VW "Dieselgate"-style hack the driver uses to pass Microsoft's checks is especially egregious. Add this to your toolkit as a signed kernel driver that allows for arbitrary shellcode execution.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/sysdream/ligolo" target="_blank">ligolo</a> is a simple and lightweight tool for establishing SOCKS5 or TCP tunnels from a reverse connection using TLS certificate with elliptical curve cryptography. Think of it as Meterpreter with Autoroute + Socks4a, but more stable and faster. This can be used stand-alone or incorporated into an in-house Go tool. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0008/" target="_blank">TA0008 Lateral Movement</a>]</li>
<li><a href="https://github.com/ajinabraham/njsscan" target="_blank">njsscan</a> is a semantic aware SAST tool that can find insecure code patterns in your Node.js applications.</li>
<li><a href="https://github.com/pry0cc/axiom" target="_blank">axiom</a> is a set of utilities for managing a small dynamic infrastructure setup for bug bounty and pentesting. If you are a Digital Ocean user and want an easy way to spin up red teaming or bug bounty infrastructure, this may be the tool for you.</li>
<li><a href="https://github.com/goichot/CVE-2020-3153" target="_blank">Cisco AnyConnect &lt; 4.8.02042 privilege escalation through path traversal</a>. It wouldn't be last week in security without a Windows local privilege escalation. This standalone C# exploit uses DLL hijacking with vpndownloader.exe, the update binary for Cisco AnyConnect. I suspect this particular exploit will be useful for many months as enterprises are slow to update their VPN clients. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/sailay1996/WerTrigger" target="_blank">WerTrigger</a> is a powerful new primitive to weaponize file write exploits. Prior to Windows 10 1909 there was the DiagHub DLL loading primitive, but since then we have only had <a href="https://github.com/itm4n/UsoDllLoader" target="_blank">UsoDllLoader</a>. Now there is another option, and when the next file write exploit is found that allows unprivileged users to write files to C:WindowsSystem32, WerTrigger will be there to pop the SYSTEM shell. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/DissectMalware/XLMMacroDeobfuscator" target="_blank">XLMMacroDeobfuscator</a> can be used to decode obfuscated XLM macros (also known as Excel 4.0 macros). It utilizes an internal XLM emulator to interpret the macros, without fully running the code. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</li>
<li><a href="https://github.com/utkusen/shotlooter" target="_blank">shotlooter</a> is a recon tool that finds sensitive data inside the screenshots uploaded to prnt.sc.</li>
<li><a href="https://github.com/fozavci/petaqc2" target="_blank">petaqc2</a> is a .NET Core/Framework RAT that uses websockets as Command &amp; Control (C2) channels. It's designed to provide a Proof of Concept (PoC) websocket malware to the adversary simulation exercises (Red &amp; Purple Team exercises).</li>
<li><a href="https://quickref.dev/" target="_blank">quickreg</a> is an experimental search engine for developers. It searches a curated subset of the web: official docs and community-driven sources. No JS, cookies, tracking, external requests or data collecting.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/s3curitybug/guardedbox" target="_blank">guardedbox</a> Online client-side manager for secure storage and secrets sharing. This could be useful for sharing scope lists, reports, or other sensitive information with clients that don't use PGP or are unable to use your encrypted email solution.</li>
<li><a href="https://github.com/jaeles-project/jaeles" target="_blank">jaeles</a> is a powerful, flexible, and easily extensible framework written in Go for building your own Web Application Scanner.</li>
<li><a href="https://github.com/foxcpp/maddy" target="_blank">maddy</a> is a composable all-in-one mail server. If you have ever spent half a day setting up a phishing mail server by hand, the short <a href="https://foxcpp.dev/maddy/tutorials/setting-up/" target="_blank">setup docs</a> for maddy should get you excited. Two commands (and DNS setup) and you have DKIM, SPF, DMARC, MTA-STS, DANE, and STARTTLS Everywhere.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
