Title: Last Week in Security (LWiS) - 2025-01-13
Date: 2025-01-13 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-01-13
Author: Erik
Summary: A Windows Rootkit (<a href="https://x.com/colehouston44" target="_blank">@colehouston44</a>), unholy PDFs (<a href="https://x.com/thomasrinsma" target="_blank">@thomasrinsma</a>), more Ivanti RCE (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), macOS exploits (<a href="https://x.com/patch1t" target="_blank">@patch1t</a> + <a href="https://x.com/MsftSecIntel" target="_blank">@MsftSecIntel</a> + <a href="https://x.com/wh1te4ever" target="_blank">@wh1te4ever</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-01-06 to 2025-01-13.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.apple.com/newsroom/2025/01/our-longstanding-privacy-commitment-with-siri/" target="_blank">Our longstanding privacy commitment with Siri</a> - After Apple agreed to pay <a href="https://www.reuters.com/legal/apple-pay-95-million-settle-siri-privacy-lawsuit-2025-01-02/" target="_blank">$95 million to settle Siri privacy lawsuit</a>, the company has put out a statement to try to calm the public. Apple denied wrongdoing in the settlement, as it was likely easier and cheaper to settle than fight the case. I suspect the plaintiffs targeted advertisements related to the conversations near their phones are due to pervasive ad tech in other aspects of their phone, not Siri. Perhaps something like: <a href="https://www.404media.co/candy-crush-tinder-myfitnesspal-see-the-thousands-of-apps-hijacked-to-spy-on-your-location/" target="_blank">Candy Crush, Tinder, MyFitnessPal: See the Thousands of Apps Hijacked to Spy on Your Location</a>.</li>
<li><a href="https://dmarcchecker.app/articles/crack-512-bit-dkim-rsa-key" target="_blank">How We Cracked a 512-Bit DKIM Key for Less Than $8 in the Cloud</a> - RSA keys shorter than 1024 bits have been considered insecure for some time, but they are still in use in some places. In 2025, it only takes 86 hours with 8 cores to crack 512-bit RSA.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/adfs-living-in-the-legacy-of-drs-c11f9b371811" target="_blank">ADFS — Living in the Legacy of DRS</a> - Adam chester with another banger. This post looks at ADFS OAuth2 support, Device Registration, Enterprise PRT, and more.</li>
<li><a href="https://www.securing.pl/en/cve-2024-50603-aviatrix-network-controller-command-injection-vulnerability/" target="_blank">CVE-2024-50603: Aviatrix Network Controller Command Injection Vulnerability</a> - The cloud marketplaces can be a great source of otherwise hard to get software for cheap research. How many unexplored systems are out there waiting for CVEs?</li>
<li><a href="https://labs.watchtowr.com/exploitation-walkthrough-and-techniques-ivanti-connect-secure-rce-cve-2025-0282/" target="_blank">Exploitation Walkthrough and Techniques - Ivanti Connect Secure RCE (CVE-2025-0282)</a> - Ivanti really needs to bring in some serious security experts to set up a fuzzing pipeline for their products, these types of vulnerabilities are not acceptable for a vendor of "secure edge" products with over a billion dollars in revenue.</li>
<li><a href="https://labs.watchtowr.com/more-governments-backdoors-in-your-backdoors/" target="_blank">Backdooring Your Backdoors - Another $20 Domain, More Governments</a> - Watchtowr was our favorite blog of 2024 and they look to have no plans on slowing down in 2025. "Hackers (and pentesters) very regularly download random code off the Internet, fire it at production systems and think they’re Neo from the Matrix." 🔥</li>
<li><a href="https://jhftss.github.io/CVE-2024-54527-MediaLibraryService-Full-TCC-Bypass/" target="_blank">CVE-2024-54527: MediaLibraryService Full TCC Bypass, Dive Deep into AMFI</a> - While Apple's Transparency Consent and Control (TCC) system is a good framework to protect user's from malware, it's not without its flaws. I would expect any well resourced attacker (i.e. nation state) would have a decent stock of TCC bypasses. PoC: <a href="https://github.com/jhftss/POC/tree/main/CVE-2024-54527" target="_blank">CVE-2024-54527</a>.</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2025/01/13/analyzing-cve-2024-44243-a-macos-system-integrity-protection-bypass-through-kernel-extensions/" target="_blank">Analyzing CVE-2024-44243, a macOS System Integrity Protection bypass through kernel extensions</a> - More macOS exploitation, this time a system integrity protection (SIP) bypass via usermode filesystems, and ironically reported by Microsoft.</li>
<li><a href="https://decoder.cloud/2025/01/09/the-almost-forgotten-vulnerable-driver/" target="_blank">The (Almost) Forgotten Vulnerable Driver</a> - An old <a href="https://www.stopzilla.com/" target="_blank">STOPzilla</a> driver allows for arbitrary write to the kernel and is not (yet) included on the Windows bad driver list, but is on <a href="https://www.loldrivers.io/" target="_blank">Living Off The Land Drivers</a> (added 2025-01-10).</li>
<li><a href="https://krebsonsecurity.com/2025/01/a-day-in-the-life-of-a-prolific-voice-phishing-crew/" target="_blank">A Day in the Life of a Prolific Voice Phishing Crew</a> - Worth watching the video in the article. The crew uses a legitimate Apple service to convince the victim they are from apple before phishing his Apple ID credentials and 2nd factor via phishing site. This is all enabled by the ability to spoof phone numbers, which due to legacy phone infrastructure (<a href="https://en.wikipedia.org/wiki/STIR/SHAKEN" target="_blank">STIR/SHAKEN</a> can't come fast enough) is trivial to do.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/cloud-pentesting/hijacking-azure-machine-learning-notebooks/" target="_blank">Hijacking Azure Machine Learning Notebooks (via Storage Accounts)</a> - Cloud companies will use their own technology to build new features, and Azure Machine Learning (AML) is no exception. It uses an Azure Storage account to store the notebooks, which can be accessed by anyone with permissions to the underlying storage, regardless of AML permissions. Potential code execution and credential access was possible due to this.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/wh1te4ever/CVE-2024-54498-PoC" target="_blank">CVE-2024-54498-PoC</a> - Escape macOS Sandbox using sharedfilelistd exploit (patched in macOS 15.2, 14.7.2, 13.7.2)</li>
<li><a href="https://github.com/SecurityInnovation/glibc_heap_exploitation_training" target="_blank">glibc_heap_exploitation_training</a> - The resources for glibc Malloc heap exploitation course by Maxwell Dulin and Security Innovation.</li>
<li><a href="https://www.trendmicro.com/en_us/research/25/a/information-stealer-masquerades-as-ldapnightmare-poc-exploit.html" target="_blank">Information Stealer Masquerades as LDAPNightmare (CVE-2024-49113) PoC Exploit</a> - This one is pretty obviously a "honeyPoC" but you should be using <a href="https://ludus.cloud/" target="_blank">Ludus</a> for PoC testing anyway.</li>
<li><a href="https://github.com/ColeHouston/Sunder" target="_blank">Sunder</a> - Windows rootkit designed to work with BYOVD exploits.</li>
<li><a href="https://github.com/Azr43lKn1ght/Rusty-PE-Packer" target="_blank">Rusty-PE-Packer</a> - A robust Windows Process Executable Packer and Launcher implementation written in Rust for Windows x64 systems.</li>
<li><a href="https://github.com/CICADA8-Research/Spyndicapped" target="_blank">Spyndicapped</a> - COM ViewLogger — new malware keylogging technique.</li>
<li><a href="https://github.com/redteamronin/EmbedInHTML" target="_blank">EmbedInHTML</a> - Embed a file in HTML and have it autodownload using JavaScript.</li>
<li><a href="https://github.com/0xNinjaCyclone/EarlyCascade/" target="_blank">EarlyCascade</a> - A PoC for Early Cascade process injection technique.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://palant.info/2025/01/13/chrome-web-store-is-a-mess/" target="_blank">Chrome Web Store is a mess</a> - Forcing a restrictive/controlled browser should be required by any business. It's fairly simple to do with Chrome or a mobile device management (MDM) solution.</li>
<li><a href="https://github.com/fin3ss3g0d/StoneKeeper" target="_blank">StoneKeeper</a> - an experimental EDR evasion framework for research purposes.</li>
<li><a href="https://th0mas.nl/2025/01/12/tetris-in-a-pdf/" target="_blank">Tetris in a PDF</a> - "I learned a bit about PDF's JavaScript API and its implementations and realized there might be just enough I/O possibility there for a simple game." The author went on to create <a href="https://github.com/ThomasRinsma/pdfdoom" target="_blank">DOOM in a PDF</a>.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 443 (+1)</p>
<p>Blogs monitored: 401 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
