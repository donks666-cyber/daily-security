Title: Last Week in Security (LWiS) - 2020-04-27
Date: 2020-04-27 11:49
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-04-27
Author: Erik
Summary: iOS and Android remote RCEs, owning centrally managed Firefox by <a href="https://twitter.com/jfmeee" target="_blank">@jfmeee</a>, a great series on malware development from <a href="https://twitter.com/0xPat" target="_blank">@0xPat</a>, <a href="https://twitter.com/sirus" target="_blank">@sirus</a> turn a GPU into a radio to steal data, and a few Windows LPEs for good measure.

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-04-20 to 2020-04-27.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bsideslv.org/covid19/" target="_blank">BSides LV</a> and DEF CON <a href="https://skytalks.info/" target="_blank">skytalks</a> announce their cancellation for 2020.</li>
<li><a href="https://www.rumble.run/pricing/" target="_blank">Rumble.run announces free tier</a>. Rumble is a scanning and asset identification product from HD Moore, founder of the Metasploit project. I have been using Rumble since the beta and it has proven to be the best tool for enumeration on engagements. The free tier gives you enough room to experiment and use on small engagements or bug bounties. After a few uses, you'll only go back to <cite>masscan</cite> and <cite>nmap</cite> for very specific scans. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1046/" target="_blank">T1046 Network Service Scanning</a>]</li>
<li><a href="https://blog.torproject.org/covid19-impact-tor" target="_blank">COVID-19’s impact on Tor</a>. Tor cut 13 of its staff and are down to 22 employees due to the lack of donations. Donate <a href="https://donate.torproject.org/" target="_blank">here</a> to help keep this privacy resource funded.</li>
<li><dl>
<dt>Mobile Bugs</dt>
<dd><ul>
<li><a href="https://blog.zecops.com/vulnerabilities/youve-got-0-click-mail/" target="_blank">You’ve Got (0-click) Mail!</a> ZecOps shows details on two different iOS mail based 0days (patched in the latest beta). The details on how they were being exploited in the wild are fuzzy but the bugs are certainly real. Close the Mail app and kill it in the background until the next iOS version drops, or update to the beta. If you are jailbroken, <a href="https://rpetrich.com/cydia/mailmend/" target="_blank">multiple</a> <a href="https://github.com/liudavicius/MailPatch" target="_blank">patches</a> are available.</li>
<li><a href="https://insinuator.net/2020/04/cve-2020-0022-an-android-8-0-9-0-bluetooth-zero-click-rce-bluefrag/" target="_blank">CVE-2020-0022 an Android 8.0-9.0 Bluetooth Zero-Click RCE – BlueFrag</a> Android 8 and 9 (<a href="https://youtu.be/lrZnZNyEqFg" target="_blank">demoed on a Galaxy S10e</a>) can be shelled without user interaction over Bluetooth. Requires and attacker to be in Bluetooth range and know the Bluetooth MAC and phone version but is very impressive.</li>
<li><a href="https://twitter.com/EveryApplePro/status/1253432816177537024" target="_blank">iOS crashes with a two character text string</a>. Not a good look for "the world's most advanced mobile operating system."</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/then/is-promise/issues/13" target="_blank">Another 1-line NPM package breaks javascript development</a>. <cite>is-promise</cite> has 3,433,289 dependencies and even had a <a href="https://github.com/then/is-promise/pull/3" target="_blank">bug</a>. The early lack of a good standard library (modern Javascript has fixed this) has caused an ecosystem of tiny packages that are maintained by unvetted developers. Let this be another reminder to <a href="https://docs.cloudfoundry.org/buildpacks/node/index.html#vendoring" target="_blank">vendor your dependencies</a> which <a href="https://stackoverflow.com/questions/45022048/why-does-npm-install-rewrite-package-lock-json/45566871#45566871" target="_blank">might work</a>!</li>
<li><a href="https://www.python.org/downloads/release/python-2718/" target="_blank">Python releases 2.7.18</a> the last release of Python 2, despite it going out of support January 1st 2020. Python 3 has been available since 2008, but if for some reason you can't upgrade, PyPy and RedHat have said they will continue supporting Python 2.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.rack911labs.com/research/exploiting-almost-every-antivirus-software/" target="_blank">Exploiting (Almost) Every Antivirus Software</a> explains a race condition between detection and file deletion that affects nearly every AV on Windows, macOS, and Linux. This allows an unprivileged user to purposely tigger the AV, then link the bad file to a different file (perhaps a file critical to the AV itself) before it is deleted. The AV fill follow this link and delete whatever it finds, perhaps changing permissions of the file or directory as well. This warrants further research (see the last entry of this section for ideas).</li>
<li><a href="https://www.mdsec.co.uk/2020/04/abusing-firefox-in-enterprise-environments/" target="_blank">Abusing Firefox in Enterprise Environments</a>. <a href="https://twitter.com/jfmeee" target="_blank">@jfmeee</a> presents his research on centrally managed Firefox and how they can be abused to achieve arbitrary file and registry writes. Even in environments with sandboxed configurations, Daniel has a way around that too.</li>
<li><a href="https://itm4n.github.io/windows-dll-hijacking-clarified/" target="_blank">Windows DLL Hijacking (Hopefully) Clarified</a> <a href="https://twitter.com/itm4n" target="_blank">@itm4n</a> takes a break from publishing Windows local privilege escalation vulnerabilities to write an in-depth article breaking down exactly what DLL Hijacking is (and isn't). [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1038/" target="_blank">T1038 DLL Search Order Hijacking</a>]</li>
<li><a href="https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html" target="_blank">Azure AD introduction for red teamers</a>. As more companies move to "the cloud" Azure AD is being seen more and more. Get familiar with how it compares to on-prem AD (less than you'd think).</li>
<li><a href="https://duo.com/labs/research/finding-radio-sidechannels" target="_blank">TEMPEST@Home - Finding Radio Frequency Side Channels</a>. If you thought last week's covert exfiltration via vibrations using case fans was tricky, Duo labs turns a GPU into a radio by changing the frequency of the shader clock. <a href="https://youtu.be/-RXo0wIZ2ao" target="_blank">Here</a> is a demo of them demodulating the GPU signals into AM. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1011/" target="_blank">T1011 Exfiltration Over Other Network Medium</a>]</li>
<li><a href="https://application.security/free-application-security-training" target="_blank">Kontra releases free application security training</a>. High quality mini-courses on common application vulnerabilities that only require a browser. Great stuff!</li>
<li><a href="https://0xpat.github.io/" target="_blank">Malware Development (parts 1-3)</a> from <a href="https://twitter.com/0xPat" target="_blank">@0xPat</a> is a detailed write up on how to minimize AV detections with C++, execute arbitrary shellcode, and persist. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0005/" target="_blank">TA0005 Defense Evasion</a>]</li>
<li><a href="https://webcache.googleusercontent.com/search?q=cache:https://secret.club/2020/04/23/directory-deletion-shell.html" target="_blank">From directory deletion to SYSTEM shell</a> is a (now deleted) post on how to turn an arbitrary file deletion bug into a SYSTEM shell on Windows using the Windows Error Reporting Service (WER) to do the dirty work. Code <a href="https://github.com/thesecretclub/ArbitraryDirectoryDeletion" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/berkgoksel/SierraOne" target="_blank">SierraOne</a> is a simple shared reverse shell over Discord. Another example of 3rd-party command and control. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1102/" target="_blank">T1102 Web Service</a>]</li>
<li><a href="https://github.com/rmdavy/pathchecker" target="_blank">pathchecker</a> checks if folders in PATH are writable. A good quick check for privilege escalation on Windows. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/earthquake/SocksOverRDP" target="_blank">SocksOverRDP</a> adds the capability of a SOCKS proxy to Terminal Services (or Remote Desktop Services). It uses a Dynamic Virtual Channel that enables communication over an open RDP connection without the need to open a new socket, connection, or a port on a firewall. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1090/" target="_blank">T1090 Connection Proxy</a>]</li>
<li><a href="https://github.com/lc/gau" target="_blank">gau</a> fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl. Use this as part of domain enumeration. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0007/" target="_blank">TA0007 Discovery</a>]</li>
<li><a href="https://github.com/mdsecactivebreach/sitrep" target="_blank">sitrep</a> is intended to provide a lightweight, extensible host triage alternative. Checks are loaded dynamically at runtime from stand-alone files. This allows operators to quickly modify existing checks, or add new checks as required. This is a great tool that gives you a quick overview of a new target. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0007/" target="_blank">TA0007 Discovery</a>]</li>
<li><dl>
<dt>Windows Local Privilege Escalation Exploits [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li><a href="https://h0mbre.github.io/atillk64_exploit" target="_blank">EOP Exploit POC for atillk64.sys by @h0mbre_</a></li>
<li><a href="https://github.com/james0x40/CVE-2020-0624" target="_blank">CVE-2020-0624 - Win32k component fails to properly handle objects in memory</a></li>
<li><a href="https://ssd-disclosure.com/ssd-advisory-cisco-anyconnect-privilege-elevation-through-path-traversal/" target="_blank">Cisco AnyConnect Privilege Elevation through Path Traversal</a> - The update functionality of the Cisco AnyConnect Secure Mobility Client for Windows is affected by a path traversal vulnerability that allows local attackers to create/overwrite files in arbitrary locations. Successful exploitation of this vulnerability allows the attacker to gain SYSTEM privileges. A Powershell PoC is shown but not provided.</li>
</ul>
</dd>
</dl>
</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
