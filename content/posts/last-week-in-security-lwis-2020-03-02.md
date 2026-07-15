Title: Last Week in Security (LWiS) - 2020-03-02
Date: 2020-03-02 11:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-03-02
Author: Erik
Summary: Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-02-24 to 2020-03-02.

<p>MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li>Brandon Azad dropped an update to his Apple iOS 13.3 exploit that <a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=1986#c5" target="_blank">includes a PAC bypass</a> [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li>Apple released their <a href="https://developer.apple.com/security-bounty/" target="_blank">security bounty program</a> details. With their recent Corellium kerfuffle, perhaps they are trying to get back into the good graces of security researches.</li>
<li>Google released a <a href="https://developers.google.com/tech-writing" target="_blank">technical writing</a> course for free. As a technical person who writes a lot and has to edit writing from others, this is a great resource.</li>
<li><a href="https://techcommunity.microsoft.com/t5/security-privacy-and-compliance/announcing-the-general-availability-of-insider-risk-management/ba-p/1180914" target="_blank">Insider Risk Management</a> is now available to all Microsoft Office 365 E5 ($35/user/month) subscribers. This tool uses ML and AI to identify insider threats while "ensuring employee privacy." [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1199/" target="_blank">T1199 Trusted Relationship</a>]</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.exodusintel.com/2020/02/24/a-eulogy-for-patch-gapping/" target="_blank">A Eulogy for Patch-Gapping Chrome</a> delves deeply into a recent Chromium issue, from patch analysis to PoC, and discusses the impact of a weekly rerelease schedule for stable Chrome which started in February. TLDR: Rapid releases makes weaponizing Ndays or "patch-gapping" very hard. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1189/" target="_blank">T1189 Drive-by Compromise</a>]</li>
<li><a href="https://twitter.com/Hexacorn/status/1231977356824383490/photo/1" target="_blank">Substitution fonts for phishing</a> enables attackers to bypass filters that trigger on obvious words by mapping letters in a simple substitution cipher in a custom font file. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1192/" target="_blank">T1192 Spearphishing Link</a>]</li>
<li>Adam Chester (XPN) <a href="https://blog.xpnsec.com/aws-lambda-redirector/" target="_blank">demonstrates</a> how to use AWS Lambda serverless functions (Golang) as redirectors for Cobalt Strike. While AWS has disabled domain fronting via CloudFront, Lambda URLs still allow it! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1172/" target="_blank">T1172 Domain Fronting</a>]</li>
<li><a href="https://ubrigens.com/posts/linking_a_microphone.html" target="_blank">CVE-2018-4184 writeup by Jakob Rieck</a> is a new writeup about an old bug. This is a prime example of there being gold buried where no one has bothered to look; 94.2% of macOS apps at the start of 2018 could access the microphone, even though the App Store Sandbox was enabled for them. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1123/" target="_blank">T1123 Audio Capture</a>]</li>
<li><a href="https://zwclose.github.io/veeamon/" target="_blank">Veeamon</a> is a writeup on the Veeam signed file system filter which enforces no ACL on its control device object, meaning anyone can use it to control IO operations on any file. This can be used to spoof requested data (file contents) and could be used as part of an exploit chain to escalate privileges or execute code. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://b4rtik.github.io/posts/evading-windefender-atp-credential-theft-kernel-version/" target="_blank">Evading WinDefender ATP credential-theft: kernel version</a> uses a vulnerable driver to patch the Windows kernel to disable kernel patch protection, then patch Defender ATP to bypass lsass dumping detection, perform the dump, and patch everything back to prevent a BSOD. If you weren't a believer in the power of kernel level code execution, this post should convince you. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1003/" target="_blank">T1003 Credential Dumping</a>]</li>
<li><a href="https://blog.cloudflare.com/securing-memory-at-epyc-scale/" target="_blank">Securing Memory at EPYC Scale</a> discusses cloudflare's benchmarks using AMD's transparent DRAM encryption. This feature adds yet another layer of security to remote bare-metal machines, and should provide more peace of mind for anyone with hardware in remote datacenters not directly under their control. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1199/" target="_blank">T1199 Trusted Relationship</a>]</li>
<li><a href="https://liberty-shell.com/sec/2020/02/25/shim-persistence/" target="_blank">Application Shimming</a> gives a good overview and examples of the windows persistence method. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1138/" target="_blank">T1138 Application Shimming</a>]</li>
<li><a href="https://github.com/skysafe/reblog/blob/master/0000-defeating-a-laptops-bios-password/README.md" target="_blank">Defeating a Laptop's BIOS Password</a> shows the lengths it takes to get around a BIOS password. If you find yourself in a similar situation, its worth checking for a <a href="https://dogber1.blogspot.com/2009/05/table-of-reverse-engineered-bios.html" target="_blank">manufacturer backdoor</a> (or the <a href="https://bios-pw.org/" target="_blank">online version</a>) before you start dumping flash.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt><a href="https://www.kb.cert.org/vuls/id/498544/" target="_blank">ZyXEL NAS pre-authentication command injection in weblogin.cgi</a> is a classic command injection in the username field. Adding a <cite>';</cite> allows for command injection.</dt>
<dd><ul>
<li>Affected devices: NAS326, NAS520, NAS540, NAS542 have patches available; NSA210, NSA220, NSA220+, NSA221, NSA310, NSA310S, NSA320, NSA320S, NSA325 and NSA325v2 are forever vulnerable. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/pry0cc/Doh365" target="_blank">Doh365</a> is a new Office365 email enumeration tool from <a href="https://twitter.com/pry0cc" target="_blank">pry0cc</a> that uses the <cite>login.microsoftonline.com/common/GetCredentialType</cite> endpoint to enumerate emails. It's subject to throttling but appears to be effective. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1087/" target="_blank">T1087 Account Discovery</a>]</li>
<li><a href="https://github.com/darkoperator/vscode-language-aggressor" target="_blank">vscode-language-aggressor</a> is a Cobalt Strike Aggressor extension for Visual Studio Code, and should come in handy for anyone who has tried to write an Aggressor script using Perl syntax highlighting. It also comes with tons of useful snippets.</li>
<li><dl>
<dt><a href="https://www.thezdi.com/blog/2020/2/24/cve-2020-0688-remote-code-execution-on-microsoft-exchange-server-through-fixed-cryptographic-keys" target="_blank">CVE-2020-0688: Remote Code Execution on Microsoft Exchange Server Through Fixed Cryptographic Keys</a> is a very interesting bug where the use of static keys (the same across every install) leads to post-auth RCE as SYSTEM. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</dt>
<dd><ul>
<li>Detection: <a href="https://github.com/Neo23x0/signature-base/blob/master/yara/vul_cve_2020_0688.yar" target="_blank">Yara rule</a></li>
<li><a href="https://github.com/Ridter/cve-2020-0688" target="_blank">PoC</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/NotSoSecure/udp-hunter" target="_blank">UDP Hunter</a> is a new python UDP scanner that covers all the common UDP services. My favorite scanning tool <a href="https://www.rumble.run/" target="_blank">rumble run</a> has limited UDP service support, so UDP Hunter is a welcome addition. A blog post  by the tool author Savan Gadhiya is <a href="https://www.gadhiyasavan.com/2020/02/udp-hunter.html" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1046/" target="_blank">T1046 Network Service Scanning</a>]</li>
<li><dl>
<dt><a href="https://github.com/duasynt/xfrm_poc" target="_blank">xfrm_poc</a> is a PoC UAF 8-byte write in the XFRM subsystem for linux 3.x-5.x kernels that leads to privilege escalation. Interestingly only a binary and detailed technical report have been released at this time. Affected distributions below. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li>Ubuntu 14.04 / 16.04 Server 4.4 LTS kernels</li>
<li>CentOS 8 4.18 kernels</li>
<li>Red Hat Enterprise Linux 8 4.18 kernels</li>
<li>Ubuntu 18.04 Server LTS 4.15 kernels</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/Y4er/CVE-2020-2551" target="_blank">CVE-2020-2551</a> is an exploit against Oracle Weblogic Server IIOP 10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0 and 12.2.1.4.0. Yet another unauthenticated RCE against Weblogic. If you are unlucky enough to have Weblogic in your environment, patch and isolate it as much as possible. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/entynetproject/mouse" target="_blank">Mouse Framework</a> is an iOS and macOS post-exploitation framework that gives you a command line session with extra functionality between you and a target machine using only a simple Mouse Payload. Mouse gives you the power and convenience of uploading and downloading files, tab completion, taking pictures, location tracking, shell command execution, escalating privileges, password retrieval, and much more.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/pkujhd/goloader" target="_blank">goloader</a> is a project that produces a binary capable of loading and running compiled golang code at runtime. It reuses its own runtime when loading compiled golang code, so the size stays small. I could see this being used for some very cool implants.</li>
<li><a href="https://css.gg/" target="_blank">css.gg</a> has 500+ minimalistic CSS icons for your web front ends. All icons are open source and availalbe under the MIT license!</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
