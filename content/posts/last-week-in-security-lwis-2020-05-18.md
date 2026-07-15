Title: Last Week in Security (LWiS) - 2020-05-18
Date: 2020-05-18 11:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-05-18
Author: Erik
Summary: A COM-based lateral movement from <a href="https://twitter.com/bohops" target="_blank">@bohops</a>, a new potato windows LPE variant from <a href="https://twitter.com/splinter_code" target="_blank">@splinter_code</a>, a local Windows brute forcer from <a href="https://twitter.com/darkcodersc" target="_blank">@DarkCoderSc</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-05-11 to 2020-05-18.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.zoom.us/wordpress/2020/05/07/zoom-acquires-keybase-and-announces-goal-of-developing-the-most-broadly-used-enterprise-end-to-end-encryption-offering/" target="_blank">Zoom Acquires Keybase and Announces Goal of Developing the Most Broadly Used Enterprise End-to-End Encryption Offering</a>. Good news for Zoom, probably bad news for keybase users.</li>
<li><a href="https://twitter.com/Zerodium/status/1260541578747064326" target="_blank">Zerodium Drops Payouts For iOS/Safari Exploits</a>. It looks like there are lots of people finding iOS exploits, perhaps due to the recent iOS 14 leak.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://vinothkumar.me/20000-facebook-dom-xss/" target="_blank">$20,000 Facebook DOM XSS</a> uses <cite>postMessage</cite> to send a payload with a javascript url element to Facebook's login button endpoint, which executes the javascript on the facebook domain. In the <a href="https://www.youtube.com/watch?v=KAnuFy2F7QA" target="_blank">demo</a> this is used to steal the user's cookies (account takeover).</li>
<li><a href="http://www.hexacorn.com/blog/2020/05/13/flash-player-background-updates-from-an-internal-server-via-mms-cfg/" target="_blank">Flash Player &amp; Background updates from an internal server via mms.cfg</a> provides a potential persistence mechanism for Windows computers running Flash (RIP).</li>
<li><a href="https://bohops.com/2020/05/12/ws-management-com-another-approach-for-winrm-lateral-movement/" target="_blank">WS-Management COM: Another Approach for WinRM Lateral Movement</a> uses the WSMAN.Automation COM object over WinRM and there are PoCs in C#, C++, Visual Basic Script, Jscript, and Powershell. Code <a href="https://github.com/bohops/WSMan-WinRM" target="_blank">here</a>.</li>
<li><a href="https://research.nccgroup.com/2020/05/14/using-sharepoint-as-a-phishing-platform/" target="_blank">Using SharePoint as a Phishing Platform</a> from nccgroup shows how SharePoint (normally a trusted domain) can be used to create phishing pages for credential harvesting.</li>
<li><a href="https://www.thirtythreeforty.net/posts/2020/05/hacking-reolink-cameras-for-fun-and-profit/" target="_blank">Hacking Reolink cameras for fun and profit</a> is a very well written and complete writeup of the process of hacking and improving an IP camera. Even if you aren't interested in embedded devices, this post is written so well you will enjoy the journey.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://rekken.github.io/2020/05/14/Security-Flaws-in-Adobe-Acrobat-Reader-Allow-Malicious-Program-to-Gain-Root-on-macOS-Silently/" target="_blank">Security Flaws in Adobe Acrobat Reader Allow Malicious Program to Gain Root on macOS Silently</a>. Another XPC logic flaw leads to local privilege escalation on macOS. Expect more of these in the near future as this technique is spreading among researchers. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><dl>
<dt>Windows Local Privilege Escalation (at what point will this need its own section?) [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li><a href="https://windows-internals.com/printdemon-cve-2020-1048/" target="_blank">PrintDemon: Print Spooler Privilege Escalation, Persistence &amp; Stealth (CVE-2020-1048 &amp; more)</a>. Legacy Windows features are the gift that keeps on giving as Print Spooler. Code <a href="https://github.com/ionescu007/PrintDemon" target="_blank">here</a>.</li>
<li><a href="https://github.com/BC-SECURITY/Invoke-PrintDemon" target="_blank">Invoke-PrintDemon</a> is a PowerShell Empire launcher PoC using <a href="https://github.com/ionescu007/PrintDemon" target="_blank">PrintDemon</a> and <a href="https://github.com/ionescu007/faxhell" target="_blank">Faxhell</a>. The module has the Faxhell dll already embedded which levages CVE-2020-1048 for privilege escalation.</li>
<li><a href="https://decoder.cloud/2020/05/11/no-more-juicypotato-old-story-welcome-roguepotato/" target="_blank">No more JuicyPotato? Old story, welcome RoguePotato!</a> the latest in the resilient "potato" line of exploits takes inspiration from PrintSpoofer (LWiS-2020-05-04). Microsoft says elevating from Local Service with SeImpersonate to SYSTEM is expected behavior so this will not be fixed! Code <a href="https://github.com/antonioCoco/RoguePotato" target="_blank">here</a>.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/hahwul/dalfox" target="_blank">dalfox</a> is a parameter analysis and XSS scanning tool written in Go. Use it to find your own 20k bounty!</li>
<li><a href="https://github.com/meme/hellscape" target="_blank">hellscape</a> is a GIMPLE obfuscator for C, C++, Go, ... all supported GCC targets and front-ends that use GIMPLE. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</li>
<li><a href="https://github.com/DarkCoderSc/win-brute-logon" target="_blank">win-brute-logon</a> - crack any Microsoft Windows users password without any privilege (Guest account included). Since Windows doesn't have a lockout on local password attempts by default, you can brute force at high speeds locally, even from Guest.</li>
<li><a href="https://github.com/Azure/Stormspotter" target="_blank">Stormspotter</a> is an Azure Red Team tool for graphing Azure and Azure Active Directory objects. Bloodhound for the cloud.</li>
<li><a href="https://github.com/sub7ee/CarbonMonoxide" target="_blank">CarbonMonoxide</a> EDR Evasion - Combination of SwampThing - TikiTorch</li>
<li><a href="https://github.com/3gstudent/SharpRDPCheck" target="_blank">SharpRDPCheck</a> checks credentials or ntlmhashes against remote Remote Desktop Protocol endpoints.</li>
<li><a href="https://github.com/Soledge/BlockEtw" target="_blank">BlockEtw</a> a injectable .NET 3.5/4 assembly to block ETW telemetry in a process. Self inject in cobalt strike to prevent telemetry on beacon.</li>
<li><a href="https://github.com/cube0x0/SharpeningCobaltStrike" target="_blank">SharpeningCobaltStrike</a> - realtime .Net v3.5/4.0 compiler for your linux Cobalt Strike C2. It generates new freshly compiled and obfuscated binaries each use.</li>
</ul>
</section>
<section id="utilities">
<h2>Utilities</h2>
<ul>
<li><a href="https://github.com/hediet/vscode-drawio" target="_blank">vscode-drawio</a> brings the great open source diagraming tool into VSCode.</li>
<li><a href="https://github.com/FiloSottile/yubikey-agent" target="_blank">yubikey-agent</a> simplifies the <a href="https://github.com/drduh/YubiKey-Guide" target="_blank">arduous yubikey setup process</a> to just a single command. This setup does not create an encrypted backup though, so a lost or broken yubikey cannot be restored.</li>
<li><a href="https://github.com/lensapp/lens" target="_blank">lens</a> is a cross platform IDE for managing Kubernetes clusters. Nothing extra needs to be installed on the pods, just run the app and start managing.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
