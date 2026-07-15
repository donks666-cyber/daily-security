Title: Last Week in Security (LWiS) - 2025-10-27
Date: 2025-10-27 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-10-27
Author: Erik
Summary: DumpGuard (<a href="https://x.com/bytewreck" target="_blank">@bytewreck</a>), GCC + VSCode (<a href="https://x.com/_winterknife_" target="_blank">@_winterknife_</a>), COM Research (<a href="https://x.com/bohops" target="_blank">@bohops</a>), Gitlab to Cloud pivot (<a href="https://x.com/0xC0rnbread" target="_blank">@0xC0rnbread</a>), function peekaboo (<a href="https://x.com/saab_sec" target="_blank">@saab_sec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-10-20 to 2025-10-27.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sharpen your Red Team skills with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p style="text-indent: 0;">Start your Red Team training with Altered Security! We offer affordable Red Team courses with enterprise-like hands-on labs and lifetime access to course materials.</p>
<p style="text-indent: 0;">Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Join more than 50,000 professionals from 130+ countries.</p>
<p style="text-indent: 0;">Enjoy 20% OFF on all courses and instructor-led bootcamps to be held in Q1 and Q2 2026. No coupon code required. Discount ends on November 1, 2025. <strong><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://cyberscoop.com/ex-l3harris-executive-accused-of-selling-trade-secrets-to-russia/" target="_blank">Ex-L3Harris executive accused of selling trade secrets to Russia</a> - $1.3 million USD in 3 years for selling trade secrets to Russia seems like a bad return on the risk. The executive was the former general manager of the company L3Harris formed after buying Azimuth Security, the company famous for "assisting" the FBI in gaining access to an iPhone in the San Bernardino case.</li>
<li><a href="https://www.theregister.com/2025/10/27/microsoft_wsus_attacks_multiple_orgs/" target="_blank">WSUS attacks hit 'multiple' orgs as Google and other infosec sleuths ring Redmond’s alarm bell</a> - Normally vulnerabilities don't make the news section, but this one seems pretty bad.</li>
<li><a href="https://www.forbes.com/sites/daveywinder/2025/10/24/the-whatsapp-1-million-hack-mystery---what-you-need-to-know/" target="_blank">The WhatsApp $1 Million Hack Mystery — What You Need To Know</a> - When zero days are this valuable, will governments let the researchers disclose them on their own terms? Or is this a case of over-hyped "low-risk bugs?"</li>
<li><a href="https://www.scientificamerican.com/article/a-solution-to-the-cias-kryptos-code-is-found-after-35-years/" target="_blank">A Solution to the CIA’s Kryptos Code Is Found after 35 Years</a> - It wasn't decrypted, but found in an archive at the Smithsonian. There's a relevant cybersecurity lesson to be learned here: Sometimes the solution/vulnerability is more easily found in a way the creator/maintainer/sysadmin didn't expect and/or involved a otherwise irrelevant 3rd party.</li>
<li><a href="https://my.f5.com/manage/s/article/K000154696" target="_blank">K000154696: F5 Security Incident</a> - "A highly sophisticated nation-state threat actor maintained long-term, persistent access to, and downloaded files from, certain F5 systems." Looks like the nation-state threat actor stole, "source code and information about undisclosed vulnerabilities." Not great to find out that a nation-state has been chilling in the network of your firewall provider. F5 says there is no evidence of modification to the software supply chain, but they also didn't have evidence of a long-term breach until August 2025 so...</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://aff-wg.org/2025/10/27/tradecraft-gardens-pic-parterre/" target="_blank">Tradecraft Garden’s PIC Parterre</a> - Mudge dropping big updates to the Tradecraft Garden, this time adding multiple dynamic function resolution targets, global variables via a .bss section shoved into slack space, and a <cite>remap</cite> option that allows easy code reuse depending on the binary target.</li>
<li><a href="https://github.com/bohops/COM-to-the-Darkside/" target="_blank">COM-to-the-Darkside</a> - Slides and resources from MCTTP 2025 Talk.</li>
<li><a href="https://risk3sixty.com/blog/attacking-self-hosted-gitlab" target="_blank">Breaking Into GitLab: Attacking and Defending Self-Hosted CI/CD Environments</a> - A Gitlab runner in EC2 with a role that grants permissions to the AWS Systems Manager allows Gitlab to Cloud pivoting.</li>
<li><a href="https://www.mdsec.co.uk/2025/10/function-peekaboo-crafting-self-masking-functions-using-llvm/" target="_blank">Function Peekaboo: Crafting self masking functions using LLVM</a> - "In this post, we will customize the LLVM compiler infrastructure to build a solution that enables self-masking capabilities for ordinary user-defined functions in a C++ source file. Self-masking means that a function remains in a masked (obfuscated or encrypted) state until it is invoked. Once execution enters the function, it is temporarily unmasked, and upon returning, it reverts back to its masked state." Code here: <a href="https://github.com/mdsecactivebreach/functionpeekaboo" target="_blank">functionpeekaboo</a>.</li>
<li><a href="https://noperator.dev/posts/on-the-money/" target="_blank">O(N) the Money: Scaling Vulnerability Research with LLMs</a> - A refreshing take on how LLMs can be used to scale vulnerability research with some open source tool releases.</li>
<li><a href="https://connormcgarr.github.io/arm64-windows-internals-basics/" target="_blank">Windows ARM64 Internals: Exception &amp; Privilege Model, Virtual Memory Management, and Windows under Virtualization Host Extensions (VHE)</a> - Connor is back to drop more windows ARM64 internals knowledge.</li>
<li><a href="https://malwaretech.com/2025/10/exif-smuggling.html" target="_blank">Look At This Photograph - Passively Downloading Malware Payloads Via Image Caching</a> - Using the browser cache to download malware payloads that a separate payload can parse and execute is pretty clever.</li>
<li><a href="https://specterops.io/blog/2025/10/21/is-kerberoasting-still-a-risk-when-aes-256-kerberos-encryption-is-enabled/" target="_blank">Is Kerberoasting Still a Risk When AES-256 Kerberos Encryption Is Enabled?</a> - TLDR: Yes. Humans are awful at picking passwords.</li>
<li><a href="https://www.synacktiv.com/en/publications/paint-it-blue-attacking-the-bluetooth-stack" target="_blank">Paint it Blue: Attacking the Bluetooth stack</a> - Getting a working, unauthenticated, remote code execution exploit against two separate Android devices is impressive, even if the vulnerability was from 2023. This is the kind of spooky exploitation that truly advanced adversaries are capable of.</li>
<li><a href="https://www.errno.fr/Bitlocker_TPM_and_PIN_privesc" target="_blank">Privescing a Laptop with BitLocker + PIN</a> - A Bitlocker + TPM + PIN (or better yet passphrase) is a good protection against physical attacks.</li>
<li><a href="https://brave.com/blog/unseeable-prompt-injections/" target="_blank">Unseeable prompt injections in screenshots: more vulnerabilities in Comet and other AI browsers</a> - Maybe steer clear of the AI browsers until the fundamental issue of untrusted data in LLM contexts is solved.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://gist.github.com/hawktrace/76b3ea4275a5e2191e6582bdc5a0dc8b" target="_blank">HawkTrace CVE-2025-59287</a> - WSUS exploit proof of concept. <a href="https://hawktrace.com/blog/CVE-2025-59287-UNAUTH" target="_blank">Blog post</a></li>
<li><a href="https://github.com/Lupovis/Honeypot-for-CVE-2025-59287-WSUS" target="_blank">Honeypot-for-CVE-2025-59287-WSUS</a> - Defensive PoC decoy for CVE-2025-59287 (WSUS) - emulates WSUS endpoints, captures request bodies and metadata, saves evidence for forensic analysis, and provides validation harness and detection rules.</li>
<li><a href="https://github.com/mubix/Find-WSUS" target="_blank">Find-WSUS</a> - Helps defenders find their WSUS configurations in the wake of CVE-2025-59287.</li>
<li><a href="https://github.com/bytewreck/DumpGuard" target="_blank">DumpGuard</a> - Proof-of-Concept tool for extracting NTLMv1 hashes from sessions on modern Windows systems. Full details: <a href="https://specterops.io/blog/2025/10/23/catching-credential-guard-off-guard/" target="_blank">Catching Credential Guard Off Guard</a>.</li>
<li><a href="https://github.com/Hypnoze57/rpc2efs" target="_blank">rpc2efs</a> - Unauthenticated start EFS service on remote Windows host (make PetitPotam great again).</li>
<li><a href="https://github.com/decoder-it/printerbugnew" target="_blank">printerbugnew</a> - The DCERPC only printerbug.py version.</li>
<li><a href="https://github.com/Flangvik/Apollo" target="_blank">Apollo</a> - A fork of the Mythic Apollo agent with support for the HTTPx C2 malleable profile.</li>
<li><a href="https://oswatcher.github.io/frontend/" target="_blank">oswatcher</a> - "Git for Operating Systems" - Track OS evolution, browse any version's filesystem, diff between any OS snapshot (release or update).</li>
<li><a href="https://github.com/winterknife/WILDBEAST" target="_blank">WILDBEAST</a> - Windows capability development using GCC and GNU Make.</li>
<li><a href="https://github.com/TheManticoreProject/gopengraph" target="_blank">gopengraph</a> - A Go library to create BloodHound OpenGraphs easily.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/noperator/slice" target="_blank">slice</a> - SAST + LLM Interprocedural Context Extractor.</li>
<li><a href="https://github.com/noperator/raink" target="_blank">raink</a> - Bleeding-edge fork of raink 🩸 Use LLMs for document ranking.</li>
<li><a href="https://github.com/0xflux/Wyrm" target="_blank">Wyrm</a> - The dragon in the dark. A red team post exploitation framework for testing security controls during red team assessments.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 465 (+3)</p>
<p>Blogs monitored: 431 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
