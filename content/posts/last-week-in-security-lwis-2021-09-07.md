Title: Last Week in Security (LWiS) - 2021-09-07
Date: 2021-09-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-09-07
Author: Erik
Summary: Mental models for offsec dev (<a href="https://twitter.com/Jackson_T" target="_blank">@Jackson_T</a>), lockscreen bypass (<a href="https://twitter.com/KLINIX5" target="_blank">@KLINIX5</a>), DLL hijacking/cloning (<a href="https://twitter.com/Jean_Maes_1994" target="_blank">@Jean_Maes_1994</a>), AV evasion framework (<a href="https://twitter.com/bb_hacks" target="_blank">@bb_hacks</a>), jailbreak detection defeat (<a href="https://twitter.com/_Kc57" target="_blank">@_Kc57</a>), Kernel drivers against EDR (<a href="https://twitter.com/synzack21" target="_blank">@synzack21</a>), Golden SAML (<a href="https://twitter.com/inversecos" target="_blank">@inversecos</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-08-23 to 2021-09-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.eff.org/deeplinks/2021/08/illinois-bought-invasive-phone-location-data-banned-broker-safegraph" target="_blank">Illinois Bought Invasive Phone Location Data From Banned Broker Safegraph</a>. I've read my cell phone and internet provider terms of service, but the issue is all the major providers have the same clauses where they can sell your data. There's no alternative that provides the same level of service while respecting customer data. I worry that since this data is "anonomyized" even measures like GDPR wouldn't be effective.</li>
<li><a href="https://www.vice.com/en/article/jg84yy/data-brokers-netflow-data-team-cymru" target="_blank">How Data Brokers Sell Access to the Backbone of the Internet</a>. More privacy nightmare fuel. Every connection to and from public IP addresses is being recorded, sold, aggregated, and analyzed. There are now full on private SIGINT systems.</li>
<li><a href="https://mirror.fro.wtf/reddit/post/3206824" target="_blank">Hackers Leak Videos of Iranian Prison</a>. This looks like a classic hacker movie scene - the screens go black then display the hacker's message full screen.</li>
<li><a href="https://msrc-blog.microsoft.com/2021/08/27/update-on-vulnerability-in-the-azure-cosmos-db-jupyter-notebook-feature/" target="_blank">Update on the vulnerability in the Azure Cosmos DB Jupyter Notebook Feature</a>. "On August 12, 2021, a security researcher reported a vulnerability in the Azure Cosmos DB Jupyter Notebook feature that could potentially allow a user to gain access to another customer’s resources by using the account’s primary read-write key." Luckily it only affected customers with the Jupyter Notebook feature enabled. For more information check out <a href="https://chaosdb.wiz.io/" target="_blank">ChaosDB</a>.</li>
<li><a href="https://citizenlab.ca/2021/08/bahrain-hacks-activists-with-nso-group-zero-click-iphone-exploits/" target="_blank">From Pearl to Pegasus Bahraini Government Hacks Activists with NSO Group Zero-Click iPhone Exploits</a>. More 0-click iOS exploit nightmare fuel.</li>
<li><a href="https://www.lawfareblog.com/solarwinds-and-holiday-bear-campaign-case-study-classroom" target="_blank">SolarWinds and the Holiday Bear Campaign: A Case Study for the Classroom</a>. This detailed-but-accessible case study of the Russian cyber espionage campaign that targeted SolarWinds is from the free <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3547103" target="_blank">Cybersecurity Law, Policy, and Institutions (version 3.1)</a>.</li>
<li><a href="https://www.theregister.com/2021/09/07/protonmail_hands_user_ip_address_police/" target="_blank">ProtonMail deletes 'we don't log your IP' boast from website after French climate activist reportedly arrested</a>. Assume your IP is being recorded by not only the site you access, but every device/government/data broker in between. Act accordingly if any of those are in your threat model.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="http://jackson-t.ca/operational-mental-models.html" target="_blank">Operational Mental Models</a>. After releasing the <a href="http://jackson-t.ca/images/210612-edr_evasion_flowchart_r2.png" target="_blank">EDR Sensor Evasion Flowchart</a>, <a href="https://twitter.com/Jackson_T" target="_blank">@Jackson_T</a> is back with another meta-assessment post about the frameworks and models for offensive research and development.</li>
<li><a href="https://halove23.blogspot.com/2021/09/zdi-21-1053-bypassing-windows-lock.html" target="_blank">ZDI-21-1053: Bypassing Windows Lock Screen</a>. The ease of access on screen reader is used once again to execute binaries on a USB and execute code even with the screen of a Windows 10 computer locked. PoC video <a href="https://www.youtube.com/watch?v=9rXXfWN0h6A" target="_blank">here</a>.</li>
<li><a href="https://itm4n.github.io/from-rpcview-to-petitpotam/" target="_blank">From RpcView to PetitPotam</a>. In this post, we will see how the information provided by this tool can be used to create a basic RPC client application in C/C++. Then, we will see how we can reproduce the trick used in the <a href="https://github.com/topotam/PetitPotam" target="_blank">PetitPotam</a> tool.</li>
<li><a href="https://labs.nettitude.com/blog/introducing-process-hiving-runpe/" target="_blank">Introducing Process Hiving &amp; RunPE</a>. "This blog introduces innovative techniques and is a must have tool for the red team arsenal. RunPE is a .NET assembly that uses a technique called Process Hiving to manually load an unmanaged executable into memory along with all its dependencies, run that executable with arguments passed at runtime, including capturing any output, before cleaning up and restoring memory to hide any trace that it was run." A solid PE runner is a must-have in ever red team toolkit. Code <a href="https://github.com/nettitude/RunPE" target="_blank">here</a>.</li>
<li><a href="https://redteamer.tips/appdata-is-a-mistake-introducing-invoke-dllclone/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=appdata-is-a-mistake-introducing-invoke-dllclone" target="_blank">%appdata% is a mistake – Introducing Invoke-DLLClone</a>. DLL hijacking isn't new but darn if it isn't effective still. The new <a href="https://github.com/jfmaes/Invoke-DLLClone" target="_blank">Invoke-DLLClone</a> is worth a look!</li>
<li><a href="https://www.trustedsec.com/blog/obsidian-taming-a-collective-consciousness/" target="_blank">Obsidian, Taming a Collective Consciousness</a>. Red team knowledge management is a topic I am all too familiar with (imagine the data that powers this blog...). This post shows a "flat" markdown note based approach that uses <a href="https://obsidian.md/" target="_blank">Obsidian</a>.</li>
<li><a href="https://www.microsoft.com/security/blog/2021/08/26/widespread-credential-phishing-campaign-abuses-open-redirector-links/" target="_blank">Widespread credential phishing campaign abuses open redirector links</a>. Most commercial email providers scan links for reputation and can prevent phishing links from being opened. Attackers are now using open redirects on "trusted" sites to bypass these protections and deliver their payloads/load their pages. These are also combined with reCAPTCHA protections to prevent automated scanning.</li>
<li><a href="https://www.inversecos.com/2021/09/backdooring-office-365-and-active.html" target="_blank">Backdoor Office 365 and Active Directory - Golden SAML</a>. This quick post shows the 8 steps to generate a golden SAML token as well as some detections.</li>
<li><a href="https://synzack.github.io/Blinding-EDR-On-Windows/" target="_blank">Blinding EDR On Windows</a>. This is a great post that brings together a lot of information about AV/EDR as well as kernel drivers, driver signing, and how to use kernel drivers against EDRs.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://blog.cloudflare.com/quick-tunnels-anytime-anywhere/" target="_blank">Quick Tunnels: Anytime, Anywhere</a>. Cloudflare tunnels are available without an account. They use 4x HTTPS connections to Cloudflare IPs to tunnel traffic to anything the cloudflared binary can reach. Consider this a more trusted version of <a href="https://ngrok.com/" target="_blank">ngrok</a>. "Unless you delete them, Tunnels can live for months." Defenders, look for update.argotunnel.com, h2.cftunnel.com, and trycloudflare.com based on my testing.</li>
<li><a href="https://github.com/duc-nt/RCE-0-day-for-GhostScript-9.50" target="_blank">RCE-0-day-for-GhostScript-9.50</a>. This 0-day exploit affects the ImageMagick with the default settings from Ubuntu repository (tested with default settings of ImageMagick on Ubuntu 20.04). More info <a href="https://twitter.com/emil_lerner/status/1430502815181463559" target="_blank">here</a>.</li>
<li><a href="https://github.com/RiccardoAncarani/LiquidSnake" target="_blank">LiquidSnake</a> is a program aimed at performing lateral movement against Windows systems without touching the disk. The tool relies on WMI Event Subscription in order to execute a .NET assembly in memory, the .NET assembly will listen for a shellcode on a named pipe and then execute it using a variation of the thread hijacking shellcode injection.</li>
<li><a href="https://github.com/t3hbb/NSGenCS" target="_blank">NSGenCS</a> is an extremely simple, yet extensible framework to evade AV with obfuscated payloads under Windows. More information at <a href="https://shells.systems/the-birth-of-nsgencs/" target="_blank">The Birth of NSGenCS</a>.</li>
<li><a href="https://posts.specterops.io/aws-readonlyaccess-not-even-once-ffbceb9fc908" target="_blank">AWS ReadOnlyAccess: Not Even Once</a>. ReadOnlyAccess sounds secure, but it can cause a false sense of security and is usually too broad for whatever is actually needed.</li>
<li><a href="https://github.com/google/security-research/security/advisories/GHSA-gg9x-v835-m48q" target="_blank">OpenBMC: remote code execution in netipmid</a>. IPMI is a very powerful interface with tons of bugs. Add this RCE to your next internal assessment bag of tricks.</li>
<li><a href="https://github.com/Kc57/iHide" target="_blank">iHide</a> is a utility for hiding jailbreaks from iOS applications. This can be a huge help when doing security assessments on applications with pesky jailbreak detection. See the <a href="https://www.trustedsec.com/blog/introducing-ihide-a-new-jailbreak-detection-bypass-tool/" target="_blank">blog post</a> for more info.</li>
<li><a href="https://github.com/aaaddress1/PR0CESS" target="_blank">PR0CESS</a> has a few projects for interesting PE loading techniques.</li>
<li><a href="https://github.com/ChrisTheCoolHut/CVE-2021-33909" target="_blank">CVE-2021-33909</a> is a Linux LPE for <a href="https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/sequoia-a-local-privilege-escalation-vulnerability-in-linuxs-filesystem-layer-cve-2021-33909" target="_blank">Sequoia</a>.</li>
<li><a href="https://github.com/threathunters-io/laurel" target="_blank">laurel</a> is a tool to transform Linux Audit logs into JSON for SIEM usage.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/packetsifter/packetsifterTool" target="_blank">packetsifterTool</a> is a tool/script that is designed to aid analysts in sifting through a packet capture (pcap) to find noteworthy traffic. Packetsifter accepts a pcap as an argument and outputs several files.</li>
<li><a href="https://github.com/pucarasec/zuthaka" target="_blank">zuthaka</a> is a collaborative free open-source Command &amp; Control integration framework that allows developers to concentrate on the core function and goal of their C2.</li>
<li><a href="https://github.com/phath0m/JadedWraith" target="_blank">JadedWraith</a> is a powerful backdoor capable of either listening on a TCP port or sniffing packets for a "magic" ICMP packet instructing the backdoor to either callback or listen.</li>
<li><a href="https://github.com/Cobalt-Strike/beacon_health_check" target="_blank">beacon_health_check</a> is an aggressor script that uses a beacon's note field to indicate the health status of a beacon.</li>
<li><a href="https://github.com/geemion/Khepri" target="_blank">Khepri</a> is a post-exploiton tool written in Golang and C++, with architecture and usage like Cobalt Strike. So much like Cobalt Strike that a casual look at the screenshot could confuse the two!</li>
<li><a href="https://github.com/ockam-network/ockam" target="_blank">ockam</a> is a library for end-to-end encryption and mutual authentication for distributed applications.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
