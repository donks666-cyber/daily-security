Title: Last Week in Security (LWiS) - 2021-06-28
Date: 2021-06-28 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-06-28
Author: Erik
Summary: Ghidra 10, Windows 11, Salesforce audit tool (<a href="https://twitter.com/exploresecurity" target="_blank">@exploresecurity</a>), XSS parser defeat (<a href="https://twitter.com/bishopfox" target="_blank">@bishopfox</a>), Mythic C2 update (<a href="https://twitter.com/its_a_feature_" target="_blank">@its_a_feature_</a>), Apache Tapestry RCE (<a href="https://twitter.com/belkahlaahmed1" target="_blank">@BelkahlaAhmed1</a>), compressed CredBandit (<a href="https://twitter.com/xenosCR" target="_blank">@xenosCR</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-06-21 to 2021-06-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blogs.windows.com/windowsexperience/2021/06/24/introducing-windows-11/" target="_blank">Introducing Windows 11</a>. Despite saying Windows 10 would be the last version of windows, Microsoft's marketing team has won and Windows 11 will be released this fall. It still uses the NT 10 kernel, and Windows 10 1507 looks very different than Windows 10 21H2, so perhaps the numbered releases are good for users and developers both (avoids the "well it works on some windows 10"). There have been rumors of <a href="https://oofhours.com/2021/06/26/new-utilities-in-windows-11/" target="_blank">new utilities</a> and <a href="https://www.extremetech.com/computing/324134-i-will-never-use-a-microsoft-account-to-log-into-my-own-pc" target="_blank">mandatory Microsoft accounts</a>, and <a href="https://secret.club/2021/06/28/windows11-tpms.html" target="_blank">taking steps against digital sovereignty with a TPM requirement</a>. At least you can bypass the TPM check during install with <a href="https://twitter.com/cadenzza_/status/1408866403743109125" target="_blank">these two registry modifications</a>. Microsoft also made sure to take shots at Apple during the re-introduction of the Microsoft App Store which allows developers to bring their own "commerce engine" and keep 100% of their revenue.</li>
<li><a href="https://www.gdatasoftware.com/blog/microsoft-signed-a-malicious-netfilter-rootkit" target="_blank">Microsoft signed a malicious Netfilter rootkit</a>. This signed kernel driver was shipping traffic to a Chinese IP. I'll be interested in the result of Microsoft's <a href="https://msrc-blog.microsoft.com/2021/06/25/investigating-and-mitigating-malicious-drivers/" target="_blank">internal investigation</a>.</li>
<li><a href="https://twitter.com/infinitelogins/status/1407432261591613445" target="_blank">Offensive Security exam retakes now $250</a>. Offensive Security's training courses have long been "the standard" but as things change, newer, more relevant courses (like <a href="https://www.zeropointsecurity.co.uk/red-team-ops" target="_blank">Red Team Ops</a>, or <a href="https://certifications.tcm-sec.com/" target="_blank">PNPT</a>) have come along to challenge the leader. Their recent moves to re-vamp their courses is good, but hiking retake prices has caused <a href="https://twitter.com/thecybermentor/status/1407554794651373570" target="_blank">some backlash</a>.</li>
<li><a href="https://www.eff.org/deeplinks/2021/06/dmca-security-researcher-statement" target="_blank">Standing With Security Researchers Against Misuse of the DMCA</a>. The Digital Millennium Copyright Act (DMCA) was outdated when it was passed in 2000, and in 2021 it makes even less sense. It's good the EFF is pushing the issue of security research before it becomes a bigger issue.</li>
<li><a href="https://security.googleblog.com/2021/06/announcing-unified-vulnerability-schema.html" target="_blank">Announcing a unified vulnerability schema for open source</a>. Google has developed a JSON standard for vulnerabilities as well as <a href="https://osv.dev/" target="_blank">site to browse them</a>.</li>
<li><a href="https://www.securityweek.com/vmware-patches-privilege-escalation-vulnerability-tools-windows?&amp;web_view=true" target="_blank">VMware Patches Privilege Escalation Vulnerability in Tools for Windows</a>. This sounds very similar to <a href="https://zeroperil.co.uk/cisco-lpe-cve-2021-1280/" target="_blank">this Cisco Immunet LPE</a>.</li>
<li><a href="https://posts.specterops.io/learning-from-our-myths-45a19ad4d077" target="_blank">Learning from our Myths</a>. Possibly the most flexible open source C2 framework Mythic gets a big update with the 2.2 release which moves to React/GraphQL as well as implementing subtasks, an OPSEC engine, translation containers, and more.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://starlabs.sg/blog/2020/06/oracle-virtualbox-vhwa-use-after-free-privilege-escalation-vulnerability/" target="_blank">Oracle VirtualBox VHWA Use-After-Free Privilege Escalation Vulnerability</a>. A kernel driver in VirtualBox was vulnerable to a use after free bug which can be exploited from a custom Windows driver to achieve code execution on the VirtualBox host machine.</li>
<li><a href="https://halove23.blogspot.com/2021/06/CVE-2021-24084-Unpatched-ID.html" target="_blank">CVE-2021-24084 An unpatched information disclosure in Microsoft Windows</a>. The mobile device management log export feature of Windows fails to impersonate the user and is vulnerable to a mount point attack. PoC <a href="https://github.com/klinix5/WindowsMDM_ID" target="_blank">here</a>.</li>
<li><a href="https://labs.bishopfox.com/tech-blog/lexss-bypassing-lexical-parsing-security-controls" target="_blank">LEXSS: Bypassing Lexical Parsing Security Controls</a>. This one is for the web app pentesters or bug bounty hunters. By using special HTML tags that leverage HTML parsing logic, it is possible to achieve cross-site scripting (XSS) even in instances where lexical parsers are used to nullify dangerous content.</li>
<li><a href="https://www.fortinet.com/blog/threat-research/spear-phishing-campaign-with-new-techniques-aimed-at-aviation-companies" target="_blank">Spear Phishing Campaign with New Techniques Aimed at Aviation Companies</a>. The VBS to drop XML and run msbuild aren't new, but the way the link was disguised in the HTML email to look like an attachment was pretty clever. Combine it with a trusted <a href="https://isc.sans.edu/forums/diary/Open+redirects+and+why+Phishers+love+them/27542/" target="_blank">open redirect</a> and you have a powerful pretext template.</li>
<li><a href="https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/23175805/Atlassian-ATO-CPR-blog-FINAL.pdf" target="_blank">A supply-chain breach: Taking over an Atlassian account</a>. This is an awesome web application hack that uses XSS, CSRF. a SameSite “Strict” bypass, HTTPOnly Bypass, and Cookie Fixation to go from a click to a full account takeover. PoC video <a href="https://www.youtube.com/watch?v=GClhS5rNga0" target="_blank">here</a>.</li>
<li><a href="https://perception-point.io/using-cve-2020-9971-to-escape-microsoft-offices-app-sandbox/" target="_blank">Using CVE-2020-9971 to escape Microsoft Office’s app sandbox</a>. This post shows a method of escaping the Office sandbox using XPC services</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_10.0_build" target="_blank">Ghidra 10.0</a>. The first major public point release and is backwards compatible with projects created in 9.x (but 10.x created projects are not backwards compatible). This is also the first public release of the debugger! Check out <a href="https://htmlpreview.github.io/?https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_10.0_build/Ghidra/Configurations/Public_Release/src/global/docs/WhatsNew.html" target="_blank">What's New</a>.</li>
<li><a href="https://github.com/xenoscr/SharpMailBOF" target="_blank">SharpMailBOF</a> is a BOF.NET program to split a file into smaller chunks and email it via a specified SMTP relay. Useful for getting large files (lsass dumps?) on slow networks using a different exfiltration method.</li>
<li><a href="https://github.com/xenoscr/compressedCredBandit" target="_blank">compressedCredBandit</a> is a modification to <a href="https://github.com/anthemtotheego/CredBandit" target="_blank">CredBandit</a> that compresses the data (using MSZIP) before sending it back which should reduce the noise on the wire.</li>
<li><a href="https://github.com/Microsoft/AttackSurfaceAnalyzer" target="_blank">AttackSurfaceAnalyzer</a> is a tool from Microsoft to help you analyze your operating system's security configuration for changes during software installation. Run it on a base install, then install all the programs your target has, re-run it, profit?</li>
<li><a href="https://github.com/nccgroup/raccoon" target="_blank">raccoon</a> is a Salesforce object access auditor. For more information, check the <a href="https://research.nccgroup.com/2021/06/28/are-you-oversharing-in-salesforce/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/kahla-sec/CVE-2021-27850_POC" target="_blank">CVE-2021-27850_POC</a> is a critical unauthenticated remote code execution vulnerability that was found in all recent versions of Apache Tapestry. By downloading the AppModule.class file you can leak the HMAC secret key used to sign all the serialized objects in Apache Tapestry.</li>
<li><a href="https://github.com/mavillon1/CVE-2021-31955-POC" target="_blank">CVE-2021-31955-POC</a>. While perhaps not useful on its own, if you have another vulnerability and are waiting on a kernel information disclosure for Windows, this is a nice PoC.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.justice.gov/criminal-ccips/page/file/1252341/download" target="_blank">Legal Considerations when Gathering Online Cyber Threat Intelligence and Purchasing Data from Illicit Sources</a>. This could be of interest if you deal in data breaches or other threat intelligence.</li>
<li><a href="https://github.com/z1pti3/jimi" target="_blank">jimi</a> is an automation first no-code platform designed and developed originally for Security Orchestration and Response. Since its launch jimi has developed into a fully fledged IT automation platform which effortlessly integrates with your existing tools unlocking the potential for autonomous IT and Security operations.</li>
<li><a href="https://useful-forks.github.io/" target="_blank">useful-forks</a> aims at increasing the discoverability of useful forks of open-source projects. GitHubs fork view is nearly worthless to determine if a fork added anything to the code or not.</li>
<li><a href="https://gitlab.com/KevinJClark/csharptoolbox/-/tree/master/WindowsBinaryReplacements" target="_blank">WindowsBinaryReplacements</a> is a nice collection of small Windows utilities in C#. These would make great "built in" commands for a custom C# rat.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
