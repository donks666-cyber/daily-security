Title: Sponsor Demo PhantomSec
Date: 1970-01-01 00:00
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: sponsor-demo-phantomsec
Author: Erik
Summary: 

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 1970-01-01 to 1970-01-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2024/01/miracleptr-protecting-users-from-use.html" target="_blank">MiraclePtr: protecting users from use-after-free vulnerabilities on more platforms</a>. The Chrome team has taken steps to protect against user-after-free vulnerabilities, and it's paying off (at the price of 1-3% worse performance)!</li>
<li><a href="https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/" target="_blank">Microsoft Actions Following Attack by Nation State Actor Midnight Blizzard</a>. Why could a non-production test tenant access senior leadership email? Interesting that these actors were looking for information about themselves. Very nation-statey.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/calling-home-get-your-callbacks-through-rbi-50633a233999" target="_blank">Calling Home, Get Your Callbacks Through RBI</a> - If you're a fan of cloudflare. This is a good read. Circumvent Remote Browser Isolation (RBI) technology during offensive assessments.</li>
<li><a href="https://www.huntress.com/blog/ransomware-deployment-attempts-via-teamviewer" target="_blank">Ransomware Deployment Attempts Via TeamViewer</a> - Traitorware is back at it again!</li>
<li><a href="https://trustedsec.com/blog/level-up-your-reporting" target="_blank">Level Up Your Reporting</a> - Fundamental concepts of writing a good offensive security report. Except you should <a href="https://bishopfox.com/blog/unredacter-tool-never-pixelation" target="_blank">never use pixelation to redact data</a>!</li>
<li><a href="https://blog.strikeready.com/blog/stealing-your-email-with-a-.txt-file/" target="_blank">Stealing your email with a .txt file</a> - Haven't seen a lot of enterprise wide use of roundcube but still a cool bug being exploited.</li>
<li><a href="https://adnanthekhan.com/2024/01/19/web3s-achilles-heel-a-supply-chain-attack-on-astar-network/" target="_blank">Web3's Achilles' Heel: A Supply Chain Attack on Astar Network</a> - Another episode of self-hosted runner exploitation. The researcher is banned from a bug bountry platform after hacking all the things... "The vulnerability allowed anyone who could fix a typo in the astarNetwork/astar repository to modify the release binaries for their validator nodes and wasm runtimes." He modified a 2 week old release with a single print statement, a release that would not be pulled by anyone following the docs to set up a validator. Seems like a reasonable PoC to me. 🤷</li>
<li><a href="https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/" target="_blank">Tales from the cloud trenches: Amazon ECS is the new EC2 for crypto mining</a> - We hope to see these more and more in the future. Technical write-ups of what threat actors are doing in the cloud can help shape our adversary simulation strategy.</li>
<li><a href="https://www.varonis.com/blog/outlook-vulnerability-new-ways-to-leak-ntlm-hashes" target="_blank">Outlook Vulnerability Discovery and New Ways to Leak NTLM Hashes</a> - Another outlook vuln fresh off the press. Windows just really, really, wants to authenticate with NTLMv2.</li>
<li><a href="https://itm4n.github.io/insomnihack-2024-cache-cache/" target="_blank">Insomni'hack 2024 CTF Teaser - Cache Cache</a>. Normally I don't post CTF write ups, but this is a unique, Windows challenge based on a real vulnerability class (and a well done write up by the challenge author).</li>
<li><a href="https://labs.watchtowr.com/the-second-wednesday-of-the-first-month-of-every-quarter-juniper-0day-revisited/" target="_blank">The Second Wednesday Of The First Month Of Every Quarter: Juniper 0day Revisited</a>. I am no longer surprised by insecure security appliances.</li>
<li><a href="https://decoder.cloud/2024/01/23/do-not-trust-this-group-policy/" target="_blank">Do not trust this Group Policy!</a>. Some interesting GPO based LPEs that won't be fixed (for now).</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/EvilGreys/Cobalt-Strike-Profiles-for-EDR-Evasion" target="_blank">Cobalt-Strike-Profiles-for-EDR-Evasion</a> - Some ideas to modify CS profiles to bypass simple EDR checks. However, if you want to use <a href="https://github.com/Tylous/SourcePoint" target="_blank">SourcePoint</a> I'm not sure I would trust the copy in this random repository...</li>
<li><a href="https://github.com/RedSiege/GraphStrike" target="_blank">GraphStrike</a> - Cobalt Strike HTTPS beaconing over Microsoft Graph API implemented as a user defined reflective loader (URDL). Appreciate the <a href="https://github.com/RedSiege/GraphStrike#why" target="_blank">Why?</a> section on this one. Better hope those Blue team network sensors have really good anomaly detection, because this will use legitimate microsoft domains for C2. However, now you have Microsoft's threat team to deal with, and there has been some discussion that they will ban accounts that conduct C2 over their API if they detect it.</li>
<li><a href="https://github.com/marcnewlin/hi_my_name_is_keyboard" target="_blank">hi_my_name_is_keyboard</a>. Zero click Bluetooth exploits for Android prior to the 2023-12-05 security patch (and Android &lt;= 10 forever). Nice close access method to get payloads on an Android phone (assuming the target won't notice their screen acting up on its own). It also works against macOS and iOS (iOS &lt; 17.2, Magic Keyboard Firmware &lt; 2.0.6) if you can trigger it exactly when the computer/phone attempts to connect with an Apple Magic keyboard via Bluetooth.</li>
<li><a href="https://github.com/febinrev/slippy-book-exploit" target="_blank">slippy-book-exploit</a> - CVE-2023-44451, CVE-2023-52076: RCE Vulnerability affected popular Linux Distros including Mint, Kali, Parrot, Manjaro etc. EPUB File Parsing Directory Traversal Remote Code Execution.</li>
<li><a href="https://github.com/febinrev/atril_cbt-inject-exploit" target="_blank">atril_cbt-inject-exploit</a> - CVE-2023-44452, CVE-2023-51698: CBT File Parsing Argument Injection that affected Popular Linux Distros.</li>
<li><a href="https://blog.washi.dev/posts/awaitfuscator/" target="_blank">Awaiting the Awaitables - Building the AwaitFuscator</a>. I doubt this is practical for programs of any complexity, but it's got to be one of the most bizarre obfuscators since the <a href="https://github.com/xoreaxeaxeax/movfuscator" target="_blank">movfuscator</a>. Code <a href="https://github.com/Washi1337/AwaitFuscator" target="_blank">here</a>.</li>
<li><a href="https://github.com/hoodoer/proxy-helper-the-sequel" target="_blank">proxy-helper-the-sequel</a> - Port/rework of proxy-helper plugin for hak5 Pineapples.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 366 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
