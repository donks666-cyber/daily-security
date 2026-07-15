Title: Last Week in Security (LWiS) - 2020-04-13
Date: 2020-04-13 06:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-04-13
Author: Erik
Summary: "Anonymous" COVID-19 contract tracing, abusing system errors for binary obfuscation, a self-paced crypto CTF, the weekly windows privesc, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-04-06 to 2020-04-13.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.hex-rays.com/products/ida-home-is-coming/" target="_blank">IDA Home is coming!</a> The "Ghidra Effect" is pushing Hex-Rays to innovate, and while details are light, this is inevitably a good thing for the reverse engineering community. However, the Home edition will only support one processor family, and is $365 a year (no decompiler). The biggest advantage is the inclusion of IDAPython while unlocks a deep community of user-created tools for IDA.</li>
<li><a href="https://www.blackberry.com/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-bb-decade-of-the-rats.pdf" target="_blank">A Decade of Rats</a> is a report from Blackberry that details advanced persistence threats targeting Linux endpoints.</li>
<li><a href="https://www.apple.com/covid19/contacttracing" target="_blank">Google and Apple team up for contract tracing</a> while trying to preserve privacy. Even with "anonymous" tracking, this data will likely be weaponized in unforeseen ways.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="http://m1el.github.io/oculus-tls-extract/" target="_blank">Extracting TLS keys from an unwilling application</a> quickly walks through the process of injecting a DLL into a process to dump SSL keys and provides the <a href="https://github.com/m1el/oculus-tls-extractor" target="_blank">code to do so</a>.</li>
<li><a href="https://itm4n.github.io/windows-server-netman-dll-hijacking/" target="_blank">Windows Server 2008R2-2019 NetMan DLL Hijacking</a> is a detailed writeup by itm4n on how a DLL hijacking vulnerability was found on all versions of Windows Server from 2008R2 to 2019 that can be triggered by a normal user with an interactive session or Network/Local Service. If you land on a Windows server box, this will more than likely get you SYSTEM. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://cryptohack.org/" target="_blank">CryptoHack</a> is a CTF platform for learning modern cryptography. Dust off <a href="https://gchq.github.io/CyberChef" target="_blank">CyberChef</a> or better yet their <a href="https://github.com/hyperreality/cryptohack-docker" target="_blank">custom docker container</a> and get to cracking! This is a very well done CTF that you can complete at your own pace.</li>
<li><a href="https://secret.club/2020/04/08/eac_integrity_check_bypass.html" target="_blank">CVEAC-2020: Bypassing EasyAntiCheat integrity checks</a> is a short article on patching the "EasyAntiCheat.sys" driver used by games like Apex Legends but is generally applicable to Windows driver reversing (think AV/EDR). [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1054/" target="_blank">T1054 Indicator Blocking</a>]</li>
<li><a href="https://www.d00rt.eus/2020/04/ebfuscation-abusing-system-errors-for.html" target="_blank">Ebfuscation: Abusing system errors for binary obfuscation</a> uses intentional errors and calls to <cite>get_last_error()</cite> to obfuscate strings in a binary. This technique flattens the call graph and can even cause errors in some disassemblers. A PoC tool is available <a href="https://github.com/d00rt/ebfuscator/" target="_blank">here</a> and the technique is reminiscent of the <a href="https://github.com/xoreaxeaxeax/movfuscator" target="_blank">movfuscator</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/bats3c/Ghost-In-The-Logs" target="_blank">Ghost-In-The-Logs</a> is a tool that leverages a kernel driver to disable Event Tracing for Windows (ETW). This can enable or disable all logging, so use it sparingly! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1054/" target="_blank">T1054 Indicator Blocking</a>]</li>
<li><a href="https://github.com/bohops/GhostBuild" target="_blank">GhostBuild</a> is a collection of simple MSBuild launchers for various GhostPack/.NET projects. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1500/" target="_blank">T1500 Compile After Delivery</a>]</li>
<li><a href="https://github.com/eddiez9/nessus-database-export" target="_blank">nessus-database-export</a> is a script to export Nessus results to a relational database for use in reports, analysis, or whatever else. This can be used to find a specific vulnerability across many scans, searching for text across all scans, seeing stats across date ranges, or as the backend for a custom web app.</li>
<li><a href="https://howto.thec2matrix.com/slingshot-c2-matrix-edition" target="_blank">Slingshot C2 Matrix Edition</a> is a virtual machine from the makers of the C2 matrix that comes with many C2 frameworks preinstalled. A SANS login is required for download. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0011/" target="_blank">TA0011 Command and Control</a>]</li>
<li><a href="https://github.com/JacobPimental/gunslinger" target="_blank">Gunslinger</a> is a hunting tool that is based around URLScan's Search API. Gunslinger can crawl URLScan for JavaScript files that match a set of user-defined rules and reports the information back to Slack. Of note, the URLScan API is free and this tool may be useful for continuous monitoring of your web properties to alert of javascript or other changes.</li>
<li><a href="https://github.com/seemoo-lab/frankenstein/" target="_blank">frankenstein</a> provides a virtual environment to fuzz wireless firmwares using the CYW20735 Bluetooth evaluation board. This is a cool tool to explore Bluetooth firmware bugs.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://about.gitlab.com/blog/2020/03/30/new-features-to-core/" target="_blank">18 GitLab features are moving to open source</a>. GitLab might be feeling the pressure from GitHub as they make their free offering even better with the following features that used to be paid-only: Related issues, Export issues, Issue board focus mode, Service desk, Web Terminal for Web IDE, File syncing to the web terminal, Design Management, Package Managers, Canary deployments, Incremental rollout, Feature flags, Deploy boards, Support for multiple Kubernetes clusters, and Network policies for container network security.</li>
<li><a href="https://github.com/projectsend/projectsend" target="_blank">Project Send</a> is a free, open source software that lets you share files with your clients, focused on ease of use and privacy. It supports clients groups, system users roles, statistics, multiple languages, detailed logs, and much more! Docker container <a href="https://github.com/linuxserver/docker-projectsend" target="_blank">here</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
