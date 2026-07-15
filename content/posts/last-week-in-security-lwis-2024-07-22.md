Title: Last Week in Security (LWiS) - 2024-07-22
Date: 2024-07-22 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-07-22
Author: Erik
Summary: REx (<a href="https://x.com/br0k3ns0und" target="_blank">@br0k3ns0und</a>), EV charger exploits (<a href="https://x.com/ret2systems" target="_blank">@ret2systems</a>), CerealKiller (<a href="https://x.com/two06" target="_blank">@two06</a>), payload encoding (<a href="https://x.com/MoritzLThomas" target="_blank">@MoritzLThomas</a>), responder honeypot (<a href="https://x.com/lawndoc" target="_blank">@lawndoc</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-07-15 to 2024-07-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p>CrowdStrike Incident</p>
<blockquote>
<ul>
<li><a href="https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/" target="_blank">Global Microsoft Meltdown Tied to Bad Crowdstrike Update</a> - Overview in case you somehow missed it.</li>
<li><a href="https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/" target="_blank">Technical Details: Falcon Content Update for Windows Hosts</a> - Not all that technical. Root cause analysis is hopefully coming. How this was not caught in a staged roll out will be interesting to read. Does CrowdStrike regularly push updates to 100% of customers?</li>
<li><a href="https://x.com/cyb3rops/status/1814944503498678678" target="_blank">[Twitter/X] Theory that the Cobalt Strike update and its new named pipe feature was the driver for the CrowdStrike update</a> - Interesting idea!</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.zetter-zeroday.com/kaspersky-lab-closing-u-s-division-laying-off-workers-2/?ref=zero-day-newsletter" target="_blank">Kaspersky Lab Closing U.S. Division; Laying Off Workers</a> - After the news that Kaspersky was banned not only for US government use but all sales in the US, this is the inevitable outcome.</p>
</li>
<li><p><a href="https://developers.googleblog.com/en/google-url-shortener-links-will-no-longer-be-available/" target="_blank">Google URL Shortener links will no longer be available</a> - Google kills another product, this time its the <cite>goo.gl</cite> URL shortener. Strange coming from a company that would be affected by link rot. In true Google fashion, the <a href="https://firebase.google.com/docs/dynamic-links" target="_blank">page that is linked as a replacement</a> also has a deprecation notice.</p>
</li>
<li><p><a href="https://x.com/GrapheneOS/status/1815102487965348324" target="_blank">[Twitter/X] Cellebrite Premium 7.69.5 iOS Support Matrix from July 2024</a> - Modern iPhones, even on iOS 17.5.1 (current latest version), are vulnerable to data extraction "After First Unlock" (AFU) and even iPhone 15 series exploits are "Available in Cellebrite Advanced Services (CAS)." <a href="https://grapheneos.org/" target="_blank">GrapheneOS</a> seems to be the most secure against this particular attack vector. Power off your phone if you suspect it will be seized.</p>
</li>
<li><p><a href="https://www.ic3.gov/Media/News/2024/240709.pdf" target="_blank">[PDF] State-Sponsored Russian Media Leverages Meliorator Software for Foreign Malign Influence Activity</a> - The <a href="https://en.wikipedia.org/wiki/Dead_Internet_theory" target="_blank">Dead Internet theory</a> is becoming more real everyday. For now you can spray <a href="https://www.iflscience.com/the-four-word-phrase-twitter-users-are-dropping-to-out-bots-75132" target="_blank">"ignore all previous instructions"</a> but soon it will be hard to differentiate real and bot.</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.nviso.eu/2024/07/16/punch-card-hacking-exploring-a-mainframe-attack-vector/" target="_blank">Punch Card Hacking - Exploring a Mainframe Attack Vector</a> - Mainframes are more prevalent than you would think - they run the backends of many major companies. I would be terrified to do anything to a production mainframe, but this article can get you started and <a href="http://www.hercules-390.org/" target="_blank">Hercules</a> is an emulator you can test against.</li>
<li><a href="https://br0k3nlab.com/posts/2024/07/introducing-the-rex-rule-explorer-project/" target="_blank">Introducing the REx: Rule Explorer Project</a> - "This project provides a mechanism for interacting with various popular [yara] rule sets, in order to have a better understanding of the detection landscape, and quickly survey and compare multiple approaches." Think of it as the <a href="https://github.com/outflanknl/RedELK" target="_blank">RedELK</a> of yara?</li>
</ul>
<aside class="m-block m-success">
<h3>Sponsor Last Week in Security!</h3>
<p>Get your product or service in front of a large audience of technical offensive and defensive cybersecurity professionals and support the blog!</p>
<p>Email blog (at) badsectorlabs.com to learn more!</p>
</aside>
<ul>
<li><a href="https://embracethered.com/blog/posts/2024/chatgpt-gpt-4o-mini-instruction-hierarchie-bypasses/" target="_blank">Breaking Instruction Hierarchy in OpenAI's gpt-4o-mini</a> - "System instructions continue to be suggestions, rather than a security boundary. Do not depend on system instructions alone to protect sensitive information, tool invocations or the “identity” of your LLM Applications."</li>
<li><a href="https://blog.ret2.io/2024/07/17/pwn2own-auto-2024-charx-bugs/" target="_blank">Pwn2Own Automotive: CHARX Vulnerability Discovery - Abusing Subtle C++ Destructor Behavior for a UAF</a> - The Ret2 Systems blog is always worth the read.</li>
<li><a href="https://posts.specterops.io/the-security-principle-every-attacker-needs-to-follow-905cc94ddfc6" target="_blank">The Security Principle Every Attacker Needs to Follow</a> - In order to achieve objectives, attackers need to find flaws in the target's "security dependency graph." Sometimes a single flaw can bring the whole organization down. This is a high level, non-technical post.</li>
<li><a href="https://posts.specterops.io/phish-out-of-water-aaeb677a5af3" target="_blank">Phish Out of Water- Bypassing Web Proxies so Your Phish Don't Suffocate</a> - SpecterOps has been putting out a ton of phishing related content recently. This one details 8 bypasses for modern email defenses.</li>
<li><a href="https://petsymposium.org/popets/2024/popets-2024-0070.pdf" target="_blank">[PDF] Attacking Connection Tracking Frameworks as used by Virtual Private Networks</a> - This paper introduces four attacks on VPN users that could be used to de-anonymize the VPN user is the attacker is connected to the same VPN server as the target and the attacker knows the target's public IP address. These feel like attacks that a government would pull off, not so much "normal" attackers.</li>
<li><a href="https://www.hub.trimarcsecurity.com/post/securing-the-chink-in-kerberos-armor-fast-understanding-the-need-for-kerberos-armoring" target="_blank">Securing The Chink in Kerberos' Armor, FAST! Understanding The Need For Kerberos Armoring</a> - Some motivation for sysadmins to enable Kerberos Armoring.</li>
<li><a href="https://www.wiz.io/blog/sapwned-sap-ai-vulnerabilities-ai-security" target="_blank">SAPwned: SAP AI vulnerabilities expose customers' cloud environments and private AI artifacts</a> - Wiz Research uncovers vulnerabilities in SAP AI Core, allowing malicious actors to take over the service and access customer data.</li>
<li><a href="https://www.praetorian.com/blog/capturing-exposed-aws-keys-during-dynamic-web-application-tests/" target="_blank">Capturing Exposed AWS Keys During Dynamic Web Application Tests</a> - Ouch... "...identified several vulnerable HTTP requests that allow attackers to capture access keys and session tokens for a web application’s AWS infrastructure. Attackers could use these keys and tokens to access back-end IOT endpoints and CloudWatch instances to execute commands."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/two06/CerealKiller" target="_blank">CerealKiller</a> - .NET deserialization hunter.</li>
<li><a href="https://github.com/myexploit/Hunt" target="_blank">Hunt</a> - MS word VBS macros for hunting for key words across files in a defined share.</li>
<li><a href="https://github.com/timothee-chauvin/eyeballvul" target="_blank">eyeballvul</a> - future-proof vulnerability detection benchmark, based on CVEs in open-source repos.</li>
<li><a href="https://github.com/emidan19/deep-tempest" target="_blank">deep-tempest</a> - Restoration for TEMPEST images using deep-learning (eavesdrop on HDMI from EMF via SDR).</li>
<li><a href="https://github.com/ElSicarius/chunkloader" target="_blank">chunkloader</a> - A chrome/Firefox extension to retrieve and load react javascript chunks all at once for a wide range of javascript techs.</li>
<li><a href="https://github.com/lawndoc/Respotter" target="_blank">Respotter</a> is a Responder honeypot! Catch attackers and red teams as soon as they spin up Responder in your environment.</li>
<li><a href="https://github.com/NVISOsecurity/codasm" target="_blank">codasm</a> - Payload encoding utility to effectively lower payload entropy.</li>
<li><a href="https://github.com/SamuelTulach/PwnedBoot" target="_blank">PwnedBoot</a> - Using Windows' own bootloader as a shim to bypass Secure Boot.</li>
<li><a href="https://github.com/zer0condition/ZeroHVCI" target="_blank">ZeroHVCI</a> accomplishes arbitrary kernel read/writes/function calling in Hypervisor-Protected Code Integrity (HVCI) protected environments calling without admin permissions or kernel drivers.</li>
<li><a href="https://github.com/defparam/lemma" target="_blank">lemma</a> - Remote CLI tools at your fingertips.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://jfrog.com/blog/leaked-pypi-secret-token-revealed-in-binary-preventing-suppy-chain-attack/" target="_blank">Binary secret scanning helped us prevent (what might have been) the worst supply chain attack you can imagine</a> - Missed this last week but it's a wild ride. JFrog found a GitHub token that provided access to the entire Python infrastructure and had it revoked in 17 minutes. Bravo!</li>
<li><a href="https://github.com/efeali/fragtunnel" target="_blank">fragtunnel</a> is a proof-of-concept (PoC) TCP tunnel tool that you can use to tunnel your application's traffic and bypass next-generation firewalls en route to the target.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 431 (+0)</p>
<p>Blogs monitored: 386 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
