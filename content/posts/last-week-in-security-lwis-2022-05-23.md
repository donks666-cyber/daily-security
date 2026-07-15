Title: Last Week in Security (LWiS) - 2022-05-23
Date: 2022-05-23 22:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-05-23
Author: Erik
Summary: Nighthawk 0.2 (<a href="https://twitter.com/MDSecLabs" target="_blank">@MDSecLabs</a>), Parallels VM escape write-up (<a href="https://twitter.com/ret2systems" target="_blank">@ret2systems</a>), Rust supply chain attack (<a href="https://twitter.com/juanandres_gs" target="_blank">@juanandres_gs</a>), DPAPI entropy capture (<a href="https://twitter.com/merrillmatt011" target="_blank">@merrillmatt011</a>), HVCI "work-around" (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), S4U2* attacks (<a href="https://twitter.com/theluemmel" target="_blank">@theluemmel</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-05-16 to 2022-05-23.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.zerodayinitiative.com/blog/2022/5/18/pwn2own-vancouver-2022-the-results" target="_blank">Pwn2Own Vancouver 2022 - The Results</a>. Always cool to see some nice 0day chains take down major names.</li>
<li><a href="https://www.vice.com/en/article/v7d9nb/department-of-justice-security-researchers-new-cfaa-policy" target="_blank">DOJ Announces It Won't Prosecute White Hat Security Researchers</a>. It's all about intent. However this is just an "agency policy" and doesn't actually change the law. Read the full PDF <a href="https://www.justice.gov/opa/press-release/file/1507126/download" target="_blank">here</a>.</li>
<li><a href="https://www.kali.org/blog/kali-linux-2022-2-release/" target="_blank">Kali Linux 2022.2 Release (GNOME 42, KDE 5.24 &amp; hollywood-activate)</a>. Nothing crazy here, just quality of life improvements, version bumps, and a "hacker" screensaver.</li>
<li><a href="https://krebsonsecurity.com/2022/05/when-your-smart-id-card-reader-comes-with-malware/" target="_blank">When Your Smart ID Card Reader Comes With Malware</a>. Supply chain attacks in equipment meant to secure systems. The ultimate trojan horse? The major user of PIVs in the US is the government, so this attack would likely land on personal (or maybe even official computers) of government employees.</li>
<li><a href="https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/" target="_blank">CrateDepression | Rust Supply-Chain Attack Infects Cloud CI Pipelines with Go Malware</a>. Supply chain attacks aren't new, and this one was likely targeting other software supply chains via their CI to expand its reach.</li>
<li><a href="https://homes.esat.kuleuven.be/~asenol/leaky-forms/leaky-forms-usenix-sec22.pdf" target="_blank">[PDF] Leaky Forms: A Study of Email and Password Exfiltration Before Form Submission</a>. "On thousands of sites email addresses are collected from login, registration and newsletter subscription forms; and sent to trackers before users submit any form or give their consent."</li>
<li><a href="https://www.cisa.gov/news/2022/05/11/joint-cybersecurity-advisory-protect-msp-providers-and-customers" target="_blank">CISA, NSA, FBI and International Cyber Authorities Issue Cybersecurity Advisory to Protect Managed Service Providers (MSP) and Customers</a>. Why hack individual companies when you can hack MSPs that have SYSTEM level access to all the endpoints in hundreds or thousands of companies?</li>
<li><a href="https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-6-1/" target="_blank">Out Of Band Update: Cobalt Strike 4.6.1</a>. Minor fixes to the 4.6 release.</li>
<li><a href="https://twitter.com/m3g9tr0n/status/1527904698690326528" target="_blank">**authenticated** PetitPotam still works even after latest updates.</a>. Windows machines just really want to authenticate to you.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2022/05/nighthawk-0-2-catch-us-if-you-can/" target="_blank">Nighthawk 0.2 - Catch Us If you Can</a>. MDSec releases the second version of their in-house C2, and is kind enough to detail its features. If you are looking for an advanced red team framework to support engagements, seriously consider Nighthawk. I haven't gotten any hands on time yet, but it sure looks impressive. If anyone at MDSec wants to hook me up with a trial contact me.</li>
<li><a href="https://blog.ret2.io/2022/05/19/pwn2own-2021-parallels-desktop-exploit/" target="_blank">Exploiting an Unbounded memcpy in Parallels Desktop</a>. This post details the development of a guest-to-host virtualization escape for Parallels Desktop on macOS, as used in a successful Pwn2Own 2021 entry to achieve code execution on a macOS host from a running a Linux guest via Parallels.</li>
<li><a href="https://posts.specterops.io/entropycapture-simple-extraction-of-dpapi-optional-entropy-6885196d54d0" target="_blank">EntropyCapture: Simple Extraction of DPAPI Optional Entropy</a>. If you've decrypted DPAPI blobs but were left with gibberish data, perhaps the encrypting appliaction was supplying optional entropy to DPAPI. The new <a href="https://github.com/merrillmatt011/EntropyCapture" target="_blank">EntropyCapture</a> uses hooks to capture that entropy so you can decrypt the blobs successfully.</li>
<li><a href="https://connormcgarr.github.io/hvci/" target="_blank">Exploit Development: No Code Execution? No Problem! Living The Age of VBS, HVCI, and Kernel CFG</a>. Hypervisor-Protected Code Integrity (HVCI) and other modern protections make kernel level code execution difficult. Connor threads the needle with kernel-mode ROP in the post and takes you along every step of the way.</li>
<li><a href="https://luemmelsec.github.io/S4fuckMe2selfAndUAndU2proxy-A-low-dive-into-Kerberos-delegations/" target="_blank">S4fuckMe2selfAndUAndU2proxy - A low dive into Kerberos delegations</a>. This post explores Kerberos delegation and ways to detect and exploit it, including the sometimes complicated S4U2self/proxy attacks.</li>
<li><a href="https://icyguider.github.io/2022/05/19/NoFix-LPE-Using-KrbRelay-With-Shadow-Credentials.html" target="_blank">No-Fix Local Privilege Escalation Using KrbRelay With Shadow Credentials</a>. This "manual" KerbRelayUp shows how the pieces work together to get a SYSTEM shell.</li>
<li><a href="https://itm4n.github.io/credential-guard-bypass/" target="_blank">Revisiting a Credential Guard Bypass</a>. Patching two offsets in LSASS can bypass credential guard, but until now, those offsets have been hard-coded in tools. This post shows how they an be dynamically located at run time. The proof of concept is <a href="https://github.com/itm4n/Pentest-Windows/blob/main/CredGuardBypassOffsets/poc.cpp" target="_blank">on GitHub</a>.</li>
<li><a href="https://securityflow.io/how-i-could-exploit-the-cve-2022-1388/" target="_blank">How I could exploit the CVE-2022-1388, F5 BIG IP iControl Authentication bypass to RCE</a>. This is the background on the biggest bug of the last few weeks.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/nccgroup/ghostrings" target="_blank">ghostrings</a> - Ghidra scripts for recovering string definitions in Go binaries. More info in this <a href="https://research.nccgroup.com/2022/05/20/tool-release-ghostrings/" target="_blank">blog post</a>.</li>
<li><a href="https://0xsp.com/offensive/mortar-loader-v2/" target="_blank">Mortar Loader v2</a>. Lots of improvements to this loader in version 2.</li>
<li><a href="https://github.com/improsec/SharpEventPersist" target="_blank">SharpEventPersist</a>. Persistence by writing/reading shellcode from Event Log.</li>
<li><a href="https://github.com/code-scrap/DynamicWrapperDotNet" target="_blank">DynamicWrapperDotNet</a>. Dynamically Loads Assembly and Calls Methods from JScript.</li>
<li><a href="https://github.com/magisterquis/bin2memfd" target="_blank">bin2memfd</a>. Encodes a program (which can be a script, despite the name) to a Perl or Python script which sticks it in a Linux memfd and runs it. The goal is to enable staged implants to be run with curl | perl, or something similar.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/KeenSecurityLab/BinAbsInspector" target="_blank">BinAbsInspector</a> - Vulnerability Scanner for Binaries.</li>
<li><a href="https://github.com/mfthomps/Labtainers" target="_blank">Labtainers</a> - Docker-based cyber lab framework.</li>
<li><a href="https://github.com/Barre/privaxy" target="_blank">privaxy</a> - (work in progress) Privaxy is the next generation tracker and advertisement blocker. It blocks ads and trackers by MITMing HTTP(s) traffic.</li>
<li><a href="https://github.com/release-argus/Argus" target="_blank">Argus</a> is a lightweight monitor to notify of new software releases via Gotify/Slack messages and/or WebHooks.</li>
<li><a href="https://github.com/scottctaylor12/Red-Lambda" target="_blank">Red-Lambda</a> - Leveraging AWS Lambda Function URLs for C2 Redirection.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+0)</p>
<p>Blogs monitored: 305 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
