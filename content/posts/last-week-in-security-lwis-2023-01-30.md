Title: Last Week in Security (LWiS) - 2023-01-30
Date: 2023-01-30 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-01-30
Author: Erik
Summary: HIVE takedown, Yandex leak, modern SEH hijacking (<a href="https://twitter.com/BillDemirkapi" target="_blank">@BillDemirkapi</a>), extending PersistAssist (<a href="https://twitter.com/Gr1mmie" target="_blank">@Gr1mmie</a> ), Docmosis Tornado horror show (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), RODC to DA (<a href="https://twitter.com/elad_shamir" target="_blank">@elad_shamir</a>), rendering Chrome to a terminal, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-01-23 to 2023-01-30.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.vice.com/en/article/qjky8d/hackers-demand-dollar10m-from-riot-games-to-stop-leak-of-league-of-legends-source-code" target="_blank">Hackers Demand $10M From Riot Games to Stop Leak of 'League of Legends' Source Code</a>. "It is alarming to know that you can be hacked within a matter of hours by an amateur-level hack." Is it?</li>
<li><a href="https://www.cisa.gov/uscert/ncas/alerts/aa23-025a" target="_blank">Protecting Against Malicious Use of Remote Monitoring and Management Software</a>. Someone at CISA finally <a href="https://www.youtube.com/watch?v=9qM2m1LZuVo" target="_blank">watched my talk on Traitorware</a>?</li>
<li><a href="https://www.justice.gov/opa/pr/us-department-justice-disrupts-hive-ransomware-variant" target="_blank">U.S. Department of Justice Disrupts Hive Ransomware Variant</a>. Don't do crimes.</li>
<li><a href="https://arseniyshestakov.com/2023/01/26/yandex-services-source-code-leak/" target="_blank">Yandex Services Source Code Leak</a>. No git history, no ML models, but lots of source code.</li>
<li><a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/" target="_blank">The Microsoft Edge team no longer offers VM image downloads for the testing of Microsoft Edge and Internet Explorer.</a>. The go-to source for quick, legitimate test VMs is gone. This on the back of the news that detection lab is not being maintained has opened a hole in the test VM/lab/management area... (stay tuned).</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://shenaniganslabs.io/2023/01/25/RODCs.html" target="_blank">At the Edge of Tier Zero: The Curious Case of the RODC</a>. Just because its read-only doesn't mean it can't lead to domain dominance.</li>
<li><a href="https://www.trustedsec.com/blog/operators-guide-to-the-meterpreter-bofloader/" target="_blank">Operator's Guide to the Meterpreter BOFLoader</a>. BOFs come to Meterpreter - they are truly the cross-C2 primitive of modern red teaming. You can run them from Python3 now with <a href="https://github.com/rkbennett/pybof" target="_blank">pybof</a>. Hell, I even put them <a href="https://gitlab.com/badsectorlabs/iscariot-suite/-/tree/main/iscariot-osquery" target="_blank">in osquery</a>.</li>
<li><a href="https://blog.assetnote.io/2023/01/24/yellowfin-auth-bypass-to-rce/" target="_blank">Exploiting Hardcoded Keys to achieve RCE in Yellowfin BI</a>. Hardcode a private key == hardcode a bad time.</li>
<li><a href="https://palant.info/2023/01/30/password-strength-explained/" target="_blank">Password strength explained</a>. This is a good explainer. Dice-chosen word-based passwords are the way to go.</li>
<li><a href="https://billdemirkapi.me/abusing-exceptions-for-code-execution-part-2/" target="_blank">Abusing Exceptions for Code Execution, Part 2</a>. This one is meaty and really cool. If you though SEH exploitation died in 2008, buckle up.</li>
<li><a href="https://fortynorthsecurity.com/blog/extending-persistassist/" target="_blank">Extending PersistAssist: Act I</a>. How to add your own modules and stick around even after a reboot.</li>
<li><dl>
<dt>Web Hacking</dt>
<dd><ul>
<li><a href="https://frycos.github.io/vulns4free/2023/01/24/0days-united-nations.html" target="_blank">Using 0days to Protect the United Nations</a>. Some web apps are frighteningly bad at security - this is one of them.</li>
<li><a href="https://shells.systems/froxlor-v2-0-6-remote-command-execution-cve-2023-0315/" target="_blank">Froxlor v2.0.6 Remote Command Execution (CVE-2023-0315)</a>. A nice authenticated RCE chain.</li>
<li><a href="https://swarm.ptsecurity.com/mybb-1-8-31-remote-code-execution-chain/" target="_blank">MyBB &lt;= 1.8.31: Remote Code Execution Chain</a>. This is just quality web app hacking.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://itm4n.github.io/insomnihack-2023-insobug/" target="_blank">Insomni'hack 2023 CTF Teaser - InsoBug</a>. CTF writeups don't usually make the blog, but this one is particularly interesting and Windows based which is extremely rare.</li>
<li><a href="https://luemmelsec.github.io/gaylord-M-FOCker-ready-to-pwn-your-MIFARE-tags/" target="_blank">gaylord M FOCker - ready to pwn your MIFARE tags</a>. If you're getting started in the RFID card space, this post will give you a quick overview of the various attacks.</li>
<li><a href="https://thalpius.com/2023/01/25/microsoft-defender-vulnerability-management-authenticated-scan-security-risks/" target="_blank">Microsoft Defender Vulnerability Management Authenticated Scan Security Risks</a>. Authenticated scans can give attackers hashes when 'Negotiate' is enabled.</li>
<li><a href="https://adamdoupe.com/blog/2023/01/23/cve-2023-23504-xnu-heap-underwrite-in-dlil-dot-c/" target="_blank">CVE-2023-23504: XNU Heap Underwrite in dlil.c</a>. "This can be triggered by a root user creating 65536 total network interfaces." Seems pretty far fetched, but a physical attack (malicious USB) is a potential vector.</li>
<li><a href="https://research.securitum.com/how-to-access-data-secured-with-bitlocker-do-a-system-update/" target="_blank">How to access data secured with BitLocker? Do a system update</a>. BitLocker effectively disables itself during updates.</li>
<li><a href="https://systemweakness.com/give-me-a-browser-ill-give-you-a-shell-de19811defa0" target="_blank">Give me a browser, I'll give you a Shell</a>. The javascript to create a browse button was neat.</li>
<li><a href="https://metalbear.co/blog/fun-with-macoss-sip/" target="_blank">Fun with macOS's SIP</a>. A nify trick to "bypass" (but not really) System Integrity Protection on macOS.</li>
<li><a href="https://0xdarkvortex.dev/hiding-in-plainsight/" target="_blank">Hiding In PlainSight - Indirect Syscall is Dead! Long Live Custom Call Stacks</a>. Loader/AV bypassers take note.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/praetorian-inc/gato" target="_blank">gato</a> GitHub Self-Hosted Runner Enumeration and Attack Tool. More information <a href="https://www.praetorian.com/blog/introducing-gato-for-ci-cd-exploitation/" target="_blank">in this post</a>.</li>
<li><a href="https://github.com/malacupa/starhound-importer" target="_blank">starhound-importer</a> - Import data from SharpHound and AzureHound using CLI instead of GUI BloodHound using "BloodHound's code". Detail <a href="https://malacupa.com/2023/01/26/starhound" target="_blank">here</a>.</li>
<li><a href="https://github.com/daddycocoaman/AzBelt" target="_blank">azbelt</a> - AAD related enumeration in Nim.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/michelcrypt4d4mus/yaralyzer#user-content-fnref-1-40a8d788b3da7d9a04f82cf79f3512b4" target="_blank">yaralyzer</a> Visually inspect and force decode YARA and regex matches found in both binary and text data. With Colors.</li>
<li><a href="https://fathy.fr/carbonyl" target="_blank">Forking Chrome to render in a terminal</a>. Simply amazing.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 423 (+0)</p>
<p>Blogs monitored: 336 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
