Title: Last Week in Security (LWiS) - 2025-08-04
Date: 2025-08-04 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-08-04
Author: Erik
Summary: AEM RCE (<a href="https://x.com/infosec_au" target="_blank">@infosec_au</a>), Intune cert abuse (<a href="https://x.com/_dirkjan" target="_blank">@_dirkjan</a>), Entra tradecraft (<a href="https://x.com/hotnops" target="_blank">@hotnops</a>), LLMs for R&amp;D (<a href="https://x.com/kyleavery_" target="_blank">@kyleavery_</a>), File System API research (<a href="https://x.com/Print3M_" target="_blank">@Print3M_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-07-28 to 2025-08-04.</p>
<aside class="m-note m-success">
<p>We'll be at DEF CON this week in the Embedded Systems Village running a mini workshop, stop by to hack an emulated IP camera hosted on <a href="https://ludus.cloud" target="_blank">Ludus</a>, get a sticker, and see the new Ludus web UI!</p>
<p>Last Week in Security will be off next week for DEF CON recovery.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://use-their-id.com/" target="_blank">Shall we see what your local MP's driving license might look like?</a> - In response to the <a href="https://www.theguardian.com/technology/2025/jul/24/what-are-the-new-uk-online-safety-rules-and-how-will-they-be-enforced" target="_blank">UK online safety rules</a>, "Tim" created a site that will generate a "satire" version of your local Member of Parliament's drivers license. It would be terrible if people used these for online age verification in the UK.</li>
<li><a href="https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html" target="_blank">Policy and Disclosure: 2025 Edition</a> - Google Project Zero will now publicly share the fact a vulnerability has been found within a week to give downstream maintainers time to prepare to update. Their <a href="https://googleprojectzero.blogspot.com/p/reporting-transparency.html" target="_blank">Reporting Transparency</a>  page has the very limited details.</li>
<li><a href="https://www.preludesecurity.com/runtime-memory-protection" target="_blank">Introducing Runtime Memory Protection</a> - The gang at Prelude is thinking about anti-virus from first principles. What if you just watched every instruction on the CPU and decided if it was malicious? With modern CPUs and the speed of consumer hardware watching every CPU instruction is doable locally now, its the determining maliciousness that will be the sticking point. However, with the team that Prelude has assembled (<a href="https://x.com/matterpreter" target="_blank">@matterpreter</a> and <a href="https://x.com/33y0re" target="_blank">@33y0re</a> to name just two), they have the brains to pull it off. They even address many of my objections directly in their very technical <a href="https://info.preludesecurity.com/hubfs/Content/Closing%20the%20Execution%20Gap.pdf" target="_blank">whitepaper</a>. How will it handle ETW <cite>EtwEventWrite</cite> patching, or operating out of JIT enabled programs like Chrome I wonder? Will be keeping track of how this develops.</li>
<li><a href="https://www.digitaldigging.org/p/the-chatgpt-confession-files" target="_blank">The ChatGPT confession files</a> - OpenAI gave people the ability to have their chats indexed by search engines (after clicking share, then clicking a check box for indexing) and users exposed some wild chats. OpenAI has since <a href="https://x.com/cryps1s/status/1951041845938499669" target="_blank">remove indexed content from the relevant search engines</a> and disabled the feature, but I was able to find 112,455 unique share links that have been archived, and there is <a href="https://www.digitaldigging.org/p/chatgpt-confessions-gone-they-are" target="_blank">some pretty dark stuff</a>. There is a standing <a href="https://cdn.arstechnica.net/wp-content/uploads/2025/06/NYT-v-OpenAI-Preservation-Order-5-13-25.pdf" target="_blank">[PDF] court order</a> forcing OpenAI to save all chat data. Probably time to look into running your own models <a href="https://www.reddit.com/r/LocalLLaMA/" target="_blank">locally</a>.</li>
<li><a href="https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/" target="_blank">Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives</a> - Scraping is <a href="https://en.wikipedia.org/wiki/HiQ_Labs_v._LinkedIn" target="_blank">legal</a>, and the line between a user browsing a website and a user instructing an AI bot to browse a website is blurring.</li>
<li><a href="https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-announces-agreement-acquire-cyberark-identity" target="_blank">Palo Alto Networks Announces Agreement to Acquire CyberArk, the Identity Security Leader</a> - $25B is the price. Big money in enterprise cybersecurity solutions it seems.</li>
<li><a href="https://www.kali.org/blog/kali-apple-container-containerization/" target="_blank">Kali Linux &amp; Containerization (Apple's Container)</a> - Native container support comes to macOS! Available now for macOS 15, with limitations, and fully supported in the next release of macOS.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://dirkjanm.io/extending-ad-cs-attack-surface-intune-certs/" target="_blank">Extending AD CS attack surface to the cloud with Intune certificates</a> - Regular users able to do ESC1 (Active Directory Certificate Services escalation attack 1) over Intune certificates given the right misconfiguration? Sign me up.</li>
<li><a href="https://specterops.io/blog/2025/07/30/entra-connect-attacker-tradecraft-part-3/" target="_blank">Entra Connect Attacker Tradecraft: Part 3</a> - "Attackers can exploit Entra Connect sync accounts to hijack device userCertificate properties, enabling device impersonation and bypassing conditional access policies. By leveraging this access, they can retrieve Intune-issued MDM and PKCS certificates, potentially compromising on-premises domains and sensitive credentials."</li>
<li><a href="https://blog.amberwolf.com/blog/2025/july/nachovpn-update---ivanti-connect-secure/" target="_blank">NachoVPN: Now With More VPN (And SYSTEM Shells) - Part 1</a> - A sneak preview of their DEF CON 33 talk, and an update to <a href="https://github.com/AmberWolfCyber/NachoVPN" target="_blank">NachoVPN</a>, a delicious, but malicious SSL-VPN server 🌮.</li>
<li><a href="https://slcyber.io/assetnote-security-research-center/struts-devmode-in-2025-critical-pre-auth-vulnerabilities-in-adobe-experience-manager-forms/" target="_blank">Struts Devmode in 2025? Critical Pre-Auth Vulnerabilities in Adobe Experience Manager Forms</a> - Adobe Experience Manager (AEM) has been a gold mine of initial access for years, and 2025 is no different.</li>
<li><a href="https://msrc.microsoft.com/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks/" target="_blank">How Microsoft defends against indirect prompt injection attacks</a> - Microsoft has done the Microsoft thing again, introduce a product (Azure AI LLMs) and then sell the security for it, "Prompt Shield."</li>
<li><a href="https://www.outflank.nl/blog/2025/07/29/accelerating-offensive-research-with-llm/" target="_blank">Accelerating Offensive R&amp;D with Large Language Models</a> - Large Language Models (LLMs) are getting to the point where with the right scaffolding and context, they can quickly find things that would take human analysis a lot of time. I appreciate Outflank sharing their work instead of creating a hyped-up product and raising $30M in funding. <a href="https://gist.github.com/kyleavery/8b604e6d5bfc30704dfee251b3bd7815" target="_blank">imapi2fs-com-stdfont-reflection.cpp</a> is the unedited proof of concept.</li>
<li><a href="https://specterops.io/blog/2025/07/31/whats-your-secret-secret-scanning-by-deeppass2/" target="_blank">What’s Your Secret?: Secret Scanning by DeepPass2</a> - Detecting secrets in large volumes of text programmatically is trickier than you might think. With some specialized data and a training, DeepPass2 (not yet released) shows improvement over standard "grep-like" tools for unstructured passwords.</li>
<li><a href="https://blog.exodusintel.com/2025/08/04/oops-safari-i-think-you-spilled-something/" target="_blank">Oops Safari, I think You Spilled Something!</a> - A detailed write up of a 2024 bug in WebKit that was part of chain that was able to get remote code execution on both macOS and iOS.</li>
<li><a href="https://print3m.github.io/blog/filejacking-initial-access-with-file-system-api" target="_blank">FileJacking – Initial Access with File System API</a> - Some foundational research on the File System API for your next phishing lure.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/x41sec/ntp-fingerprinter" target="_blank">ntp-fingerprinter</a> - Script to fingerprint NTP servers.</li>
<li><a href="https://github.com/dirkjanm/scepreq" target="_blank">scepreq</a> - SCEP request tool for AD CS and Intune.</li>
<li><a href="https://github.com/kyxiaxiang/CobaltStrikeBeaconCppSource" target="_blank">CobaltStrikeBeaconCppSource</a> - Out-of-the-box CobaltStrike Beacon source code use C++.</li>
<li><a href="https://github.com/charmbracelet/crush" target="_blank">crush</a> - The glamorous AI coding agent for your favorite terminal 💘.</li>
<li><a href="https://github.com/G0ldenGunSec/SCCM_SQL_Collector" target="_blank">SCCM_SQL_Collector</a> - PoC script to demonstrate collection of SCCM attack paths that can be viewed in BH with OpenGraph.</li>
<li><a href="https://github.com/G0ldenGunSec/OpenImporter" target="_blank">OpenImporter</a> - Middleware utility for enriching and uploading data gathered with arbitrary collectors.</li>
<li><a href="https://github.com/SpecterOps/MSSQLHound" target="_blank">MSSQLHound</a> - PowerShell collector for adding MSSQL attack paths to BloodHound with OpenGraph.</li>
<li><a href="https://github.com/dexter-xD/TinyRequest" target="_blank">TinyRequest</a> - Lightweight HTTP client with modern GUI for Linux.</li>
<li><a href="https://github.com/jeanlucdupont/EXEfromCER" target="_blank">EXEfromCER</a> - PoC that downloads an executable from a public SSL certificate.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/x41sec/EncroCam/" target="_blank">EncroCam</a> - Privacy security camera based on commodity hardware.</li>
<li><a href="https://github.com/jeffcaldwellca/mkcertWeb" target="_blank">mkcertWeb</a> - Web based user interface for mkcert CLI internal CA.</li>
<li><a href="https://github.com/zakharb/labshock" target="_blank">labshock</a> - OT Security Lab for ICS networks.</li>
<li><a href="https://github.com/CroodSolutions/AutoRMM/tree/main" target="_blank">AutoRMM</a> - AutoRMM is a collection of scripts and instructions we are organizing, to test delivery mechanisms for RMM and screen sharing tools, along with post exploitation strategies for blue and red teams wanting to more realistically simulate adversary capabilities using these strategies.</li>
<li><a href="https://www.decisionproblem.com/paperclips/index2.html" target="_blank">Universal Paperclips</a> - A shockingly fun text based "game" based on the <a href="https://en.wikipedia.org/wiki/Instrumental_convergence#Paperclip_maximizer" target="_blank">Paperclip maximizer</a> thought experiment.</li>
<li><a href="https://malwaretech.com/2025/08/every-reason-why-i-hate-ai.html" target="_blank">Every Reason Why I Hate AI and You Should Too</a> - The praise for Apple is interesting, given that Siri has been an embarrassment for years. "I, too, could score 100% on a multiple-choice exam if you let me Google all the answers." Yes, but could you <a href="https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/" target="_blank">achieve gold-medal standard at the International Mathematical Olympiad</a>? I don't think so, even with a year to do it an not 8 hours. Like most things, the "truth" (whatever that is) is probably somewhere in the middle of the hype-train conductors and the doomers.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+0)</p>
<p>Blogs monitored: 424 (+0)</p>
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
