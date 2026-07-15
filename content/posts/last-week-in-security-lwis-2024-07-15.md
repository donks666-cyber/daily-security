Title: Last Week in Security (LWiS) - 2024-07-15
Date: 2024-07-15 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-07-15
Author: Erik
Summary: HavocC2 SSRF (<a href="https://x.com/_chebuya" target="_blank">@_chebuya</a>), PDF rendering diffs (<a href="https://x.com/d4d89704243" target="_blank">@d4d89704243</a>), Windows phishing 0day (<a href="https://x.com/_cpresearch_" target="_blank">@_CPResearch_</a>), 3x Sharepoint RCEs (<a href="https://x.com/testanull" target="_blank">@testanull</a>), Dynamics 365 flaws (<a href="https://x.com/frycos" target="_blank">@frycos</a>), Mythic 3.3 Beta (<a href="https://x.com/its_a_feature_" target="_blank">@its_a_feature_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-07-08 to 2024-07-15.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.cloudflare.com/application-security-report-2024-update" target="_blank">Application Security report: 2024 update</a> - Some interesting data in this report, especially that Cloudflare saw exploitation attempts for the JetBrains TeamCity authentication bypass just 22 minutes after proof-of-concept code was published. Perhaps the threat actors had an <a href="https://ludus.cloud" target="_blank">automated lab</a> and could quickly test/modify the PoC, but more likely they just YOLO'd it.</li>
<li><a href="https://www.businessinsider.com/google-close-to-23-billion-deal-wiz-cybersecurity-startup-2024-7" target="_blank">Google is closing in on its biggest deal: a New York startup that's less than 4 years old</a> - 4 years to (a rumored) $23 billion acquisition has to be a record for unicorn startup success. Congratulations to the Wiz team (assuming the rumors are true).</li>
</ul>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Learn Azure and on-prem Red Teaming</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Red Ream training with us! <a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Altered Security</a> offers multiple Red Team course with affordable and enterprise-like hands-on labs.
Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more.
Our courses and labs are designed by experts who have more than a decade's experience of training and speaking at Black Hat USA, DEF CON and other respected conferences.
Join more than 30K professionals from 130+ countries.</p>
<p>Enjoy <strong>20% OFF</strong> on all courses using <span style="color: #3bd267;"><strong>HackerSummer20OFF</strong></span> (Stripe) from 1st July to 22nd July 2024.</p>
</aside><ul>
<li><a href="https://krebsonsecurity.com/2024/07/hackers-steal-phone-sms-records-for-nearly-all-att-customers/" target="_blank">Crooks Steal Phone, SMS Records for Nearly All AT&amp;T Customers</a> - Another day, another breach. And another reason not to use SMS for multifactor authentication unless it is the only choice.</li>
<li><a href="https://techcrunch.com/2024/07/10/apple-alerts-iphone-users-in-98-countries-to-mercenary-spyware-attacks/" target="_blank">Apple warns iPhone users in 98 countries of spyware attacks</a> - This is the second round of notifications to go out. If you may be a target, turn on lockdown mode, and reboot your phone often.</li>
<li><a href="https://posts.specterops.io/mythic-3-3-beta-rise-of-the-events-6aeb84aa6fed" target="_blank">Mythic 3.3 Beta: Rise of the Events</a> - Mythic, the popular open source C2, is getting some great new features. The new eventing system looks awesome.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.cloudflare.com/radius-udp-vulnerable-md5-attack" target="_blank">RADIUS/UDP vulnerable to improved MD5 collision attack</a> - A MiTM attack is possible against RADIUS servers that use UDP in Password Authentication Protocol (PAP) mode. The RADIUS authors in the 90's likely did not anticipate that an MD5 collision would be practical to execute in under 30 seconds - the default timeout for many devices. However, with some <a href="https://github.com/cr-marcstevens/hashclash/pull/37" target="_blank">fancy cryptography</a> and a pile of GPUs, it's possible in 2024. Full PDF here: <a href="https://www.blastradius.fail/pdf/radius.pdf" target="_blank">RADIUS/UDP Considered Harmful</a>.</li>
<li><a href="https://codeanlabs.com/blog/research/cve-2024-29511-abusing-ghostscripts-ocr-device/" target="_blank">CVE-2024-29511 - Abusing Ghostscript's OCR device</a> - More Ghostscript exploitation from <a href="https://x.com/thomasrinsma" target="_blank">@thomasrinsma</a> at Codean Labs that allows file read and write outside the sandbox.</li>
<li><a href="https://portswigger.net/research/fickle-pdfs-exploiting-browser-rendering-discrepancies" target="_blank">Fickle PDFs: exploiting browser rendering discrepancies</a> - This could be useful for phishing if you knew the browsers used by different users, or if an email security gateway used a specific browser to render PDFs and the users a different browser.</li>
<li><a href="https://research.checkpoint.com/2024/resurrecting-internet-explorer-threat-actors-using-zero-day-tricks-in-internet-shortcut-file-to-lure-victims-cve-2024-38112/" target="_blank">Resurrecting Internet Explorer: Threat Actors Using Zero-Day Tricks in Internet Shortcut File to Lure Victims (CVE-2024-38112)</a> - Some nifty tricks to obscure HTA execution on Windows 10/11. Patched in the 2024-07 patch tuesday.</li>
<li><a href="https://palant.info/2024/07/15/how-insecure-is-avast-secure-browser/" target="_blank">How insecure is Avast Secure Browser?</a> - Spoiler: its just chrome wrapped in ads and data collection.</li>
<li><a href="https://embracethered.com/blog/posts/2024/chatgpt-persistent-denial-of-service/" target="_blank">Sorry, ChatGPT Is Under Maintenance: Persistent Denial of Service through Prompt Injection and Memory Attacks</a> - This could be used to disrupt ChatGPT once it scrapes your site. Would imbedding the "DoS" prompt in html comments be enough to do it I wonder.</li>
<li><a href="https://frycos.github.io/vulns4free/2024/07/10/dynamics-ups-and-downs.html" target="_blank">Dynamics 365 Business Central - A Journey With Ups and Downs</a> - A lesser known on-prem Microsoft product, "Dynamics 365 Business Central" is a .NET application with (now patched) unauthenticated file write vulnerability. Good .NET code audit content.</li>
<li><a href="https://blog.syss.com/posts/voip-deskphone-firmware-security/" target="_blank">Firmware Security: Alcatel-Lucent ALE-DeskPhone</a> - From firmware download to shell and two vulnerabilities, this is solid walkthrough of embedded device hacking.</li>
<li><a href="https://dayzerosec.com/blog/2024/07/11/getting-started-2024.html" target="_blank">Getting Started with Exploit Development</a> - A great resource for anyone looking to get started in binary exploitation.</li>
<li><a href="https://blog.chebuya.com/posts/server-side-request-forgery-on-havoc-c2/" target="_blank">Unauthenticated SSRF on Havoc C2 teamserver via spoofed demon agent</a> - There is something extra awesome about an exploit against a command and control framework. This was no simple exploit, and the walkthrough is great.</li>
<li><a href="https://www.sprocketsecurity.com/resources/gigaproxy" target="_blank">One Proxy to Rule Them All</a> - A powerful tool to help you bypass Web Application Firewalls (WAFs) during external penetration tests and bug bounty programs, you're in the right place.</li>
<li><a href="https://syntax-err0r.github.io/Silently_Install_Chrome_Extension.html" target="_blank">Silently Install Chrome Extension For Persistence</a> - Attack surface moves to the browser more and more each day!</li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-193a" target="_blank">CISA Red Team's Operations Against a Federal Civilian Executive Branch Organization Highlights the Necessity of Defense-in-Depth</a> - CISA's "SILENTSHIELD" team rekt a Federal Civilian Executive Branch (FCEB) organization. Good read to understand how an APT would get into and move laterally though a large organization.</li>
<li><a href="https://0xv1n.github.io/posts/sessionenumeration/" target="_blank">Remote Session Enumeration via Undocumented Windows APIs</a> - This article details how to implement remote session enumeration on Windows systems using undocumented WinStation APIs, replicating qwinsta functionality through custom C++ code.</li>
<li><a href="https://www.elastic.co/security-labs/false-file-immutability" target="_blank">Introducing a New Vulnerability Class: False File Immutability</a> - "Previously-unnamed" class of Windows vulnerabilities? 🧐</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://ssd-disclosure.com/ssd-advisory-sonicwall-sma100-stored-xss-to-rce/" target="_blank">SSD Advisory - Sonicwall Sma100 Stored XSS to RCE</a> - This one is particularly bad as the stored XSS can be added with a failed logon and triggered when an admin browsers to the <cite>Log / View</cite> page. After that a command injection gets remote code execution.</li>
<li><a href="https://github.com/mbadanoiu/CVE-2024-22274" target="_blank">CVE-2024-22274</a> - Authenticated Remote Code Execution in VMware vCenter Server.</li>
<li><a href="https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC" target="_blank">MS-SharePoint-July-Patch-RCE-PoC</a> PoCs for CVE-2024-38094, CVE-2024-38024, and CVE-2024-38023.</li>
<li><a href="https://github.com/CERT-Polska/mailgoose?tab=readme-ov-file" target="_blank">mailgoose</a> - A web application that allows the users to check whether their SPF, DMARC and DKIM configuration is set up correctly.</li>
<li><a href="https://github.com/exploits-forsale/collateral-damage" target="_blank">collateral-damage</a> - Kernel exploit for Xbox SystemOS using CVE-2024-30088.</li>
<li><a href="https://github.com/rzte/pdf-exploit" target="_blank">pdf-exploit</a> - pdf exploit integration.</li>
<li><a href="https://github.com/Sprocket-Security/gigaproxy" target="_blank">gigaproxy</a> - One proxy to rule them all.</li>
<li><a href="https://github.com/CICADA8-Research/IHxExec" target="_blank">IHxExec</a> - Process injection alternative.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/pumpbin/pumpbin" target="_blank">pumpbin</a> - 🎃 PumpBin is an Implant Generation Platform.</li>
<li><a href="https://github.com/DefGuard/defguard" target="_blank">defguard</a> - Enterprise, fast, secure VPN &amp; SSO platform with hardware keys, 2FA/MFA.</li>
<li><a href="https://zed.dev/blog/zed-on-linux" target="_blank">Linux when? Linux now.</a> - Zed (a code editor) is now available for Linux.</li>
<li><a href="https://uuid.pirate-server.com/" target="_blank">World's most complete UUID database.</a> - World's most complete UUID database.</li>
<li><a href="https://escapecollective.com/exclusive-tour-riders-are-inhaling-carbon-monoxide-in-super-altitude-recipe/" target="_blank">Exclusive: Tour riders are inhaling carbon monoxide to optimise altitude training</a> - Cycling is a sport famous for its "hacks" (cheating, doping, etc) second only to Formula 1. Riders may be purposely inhaling precisely dosed carbon monoxide to get "super altitude" training. Sounds dangerous.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 431 (+1)</p>
<p>Blogs monitored: 386 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
