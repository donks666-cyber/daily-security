Title: Last Week in Security (LWiS) - 2023-08-07
Date: 2023-08-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-08-07
Author: Erik
Summary: Epic rewards point hack (<a href="https://twitter.com/samwcyo" target="_blank">@samwcyo</a>), blinding auditd (<a href="https://twitter.com/qtc_de" target="_blank">@qtc_de</a>), attacking an EDR (<a href="https://twitter.com/dottor_morte" target="_blank">@dottor_morte</a>), expect scripting (<a href="https://twitter.com/cedowens" target="_blank">@cedowens</a>), and more!

<aside class="m-note m-warning">
<h3>DEF CON 31</h3>
<p>LWiS will be taking a week off next week. I'll be in Vegas if you want to discuss the state of offensive security, your greatest hack, or anything else!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-07-31 to 2023-08-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2023/08/summary-mte-as-implemented.html" target="_blank">Summary: MTE As Implemented</a>. Good series from Project Zero on ARM's new memory tagging extension coming to v9 chips. TLDR: memory exploitation is getting harder. However, just like pointer authentication in iOS/macOS, exploitation is of course still possible.</li>
<li><a href="https://msrc.microsoft.com/blog/2023/08/microsoft-bug-bounty-program-year-in-review-13.8m-in-rewards/" target="_blank">Microsoft Bug Bounty Program Year in Review: $13.8M in Rewards</a>. Maybe they should have spent more? <a href="https://www.linkedin.com/pulse/microsoftthe-truth-even-worse-than-you-think-amit-yoran" target="_blank">Microsoft... The Truth Is Even Worse Than You Think</a>.</li>
<li><a href="https://www.rapid7.com/blog/post/2023/08/02/cve-2023-35082-mobileiron-core-unauthenticated-api-access-vulnerability/" target="_blank">CVE-2023-35082 - MobileIron Core Unauthenticated API Access Vulnerability</a>. Who needs ARM MTE when you can just browse to a link and get access to all the endpoints of an organization.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-exploit-bleedingpipe-rce-to-target-minecraft-servers-players/" target="_blank">Hackers exploit BleedingPipe RCE to target Minecraft servers, players</a>. With huge user bases, games are becoming real targets for hackers.</li>
<li><a href="https://posts.specterops.io/your-new-best-friend-introducing-bloodhound-community-edition-cb908446e270" target="_blank">Your new best friend: Introducing BloodHound Community Edition</a>. "On August 8, 2023, BloodHound CE will be made available in its entirety." Hyped!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://samcurry.net/points-com/" target="_blank">Leaked Secrets and Unlimited Miles: Hacking the Largest Airline and Hotel Rewards Platform</a>. Sam Curry doesn't miss - great web app hacking content.</li>
<li><a href="https://bishopfox.com/blog/analysis-exploitation-cve-2023-3519" target="_blank">Analysis and Exploitation of CVE-2023-3519</a>. The Citrix ADC RCE (exploit <a href="https://github.com/BishopFox/CVE-2023-3519" target="_blank">here</a>) is possible because exploit mitigation from 1997 (stack canaries) are not present on network edge devices. Forget about ARM memory tagging, let's just do some basics.</li>
<li><a href="https://bishopfox.com/blog/breaking-fortinet-firmware-encryption" target="_blank">Breaking Fortinet Firmware Encryption</a>. Some great cryptanalysis to decrypt firmware images. This feels like a CTF challenge in real life.</li>
<li><a href="https://code-white.com/blog/2023-08-blindsiding-auditd-for-fun-and-profit/" target="_blank">Blindsiding auditd for Fun and Profit</a>. Very legit post-ex Linux tools and great explanation.</li>
<li><a href="https://riccardoancarani.github.io/2023-08-03-attacking-an-edr-part-1/" target="_blank">Attacking an EDR - Part 1</a>. What if you found an allowlisted process and spawned it suspended and then injected. Turns out, it works!</li>
<li><a href="https://llm-attacks.org/" target="_blank">Universal and Transferable Adversarial Attacks on Aligned Language Models</a>. Automated attacks on LLMs.</li>
<li><a href="https://posts.specterops.io/challenges-in-post-exploitation-workflows-2b3469810fe9" target="_blank">Challenges In Post-Exploitation Workflows</a>. My body is ready. Inject <a href="https://github.com/SpecterOps/Nemesis" target="_blank">Nemesis</a> (currently 404s) into my veins. Man I hope this delivers, but the gang at Specter Ops has a great track record.</li>
<li><a href="https://labs.guard.io/phishforce-vulnerability-uncovered-in-salesforces-email-services-exploited-for-phishing-32024ad4b5fa" target="_blank">“PhishForce” — Vulnerability Uncovered in Salesforce’s Email Services Exploited for Phishing Facebook Accounts In-The-Wild</a>. Any system that can send email will be used for phishing.</li>
<li><a href="https://research.aurainfosec.io/pentest/hook-line-and-phishlet/" target="_blank">Hook, Line, and Phishlet: Conquering AD FS with Evilginx</a>.   The EvilNginx hype continues. Phishing ADFS in your next assessment? This one's for you.</li>
<li><a href="https://nostarch.com/download/EvadingEDR_chapter6.pdf" target="_blank">[PDF] Evading EDR Chapter 6</a>. One chapter of Matt Hand’s upcoming book is available now. It’s also open for early access, and rumor has it this blog gets a mention!</li>
<li><a href="https://pentera.io/resources/whitepapers/the-lolbas-odyssey-finding-new-lolbas-and-how-you-can-too/" target="_blank">[PDF] The LOLBAS Odyssey: Finding New LOLBAS, and How You Can, Too</a>. We <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">love LOLBAS</a> and this paper proposes and interesting automation framework for finding them.</li>
<li><a href="https://cedowens.medium.com/what-to-expect-when-youre-expecting-purple-team-edition-c6879655fe1" target="_blank">What To Expect When You're “Expecting" — Purple Team Edition</a>. A lot of talks recently about the different types of purple team engagements, the value of purple teaming, etc. Nice to see Cedric dropping some wisdom for us on execution of a purple team.</li>
<li><a href="https://www.o3c.no/knowledge/abusing-app-role-assignment-actions-in-entra-id" target="_blank">Abusing app role assignment actions in Entra ID</a>. This blog provides some insight into the potential security risks and implications associated with the new action in the Entra ID role. Who else is monitoring these changes? 🤔</li>
<li><a href="https://blog.sygnia.co/guarding-the-bridge-new-attack-vectors-in-azure-ad-connect" target="_blank">Guarding the Bridge: New Attack Vectors in Azure AD Connect</a>. MITM or ADCS + Azure AD Connect can lead to NT hashes. Good summary from some existing work on attacking Azure AD Connect.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/codewhitesec/daphne" target="_blank">daphne</a> - Proof-of-Concept to evade auditd by tampering via ptrace.</li>
<li><a href="https://github.com/codewhitesec/apollon" target="_blank">apollon</a> - Proof-of-Concept to evade auditd by writing /proc/PID/mem.</li>
<li><a href="https://github.com/lissy93/web-check" target="_blank">web-check</a> - 🌐 All-in-one OSINT tool for analyzing any website.</li>
<li><a href="https://github.com/hashicorp-forge/grove/" target="_blank">grove</a> - A Software as a Service (SaaS) log collection framework from Hashicorp.</li>
<li><a href="https://github.com/giuseppelt/EmailFlare" target="_blank">EmailFlare</a> - Send emails from your domain through Cloudflare for free. Self host on your account.</li>
<li><a href="https://github.com/Cyb3r-Monk/ACCD/tree/main" target="_blank">ACCD</a> - Active C&amp;C Detector. Includes a deck on how it works.</li>
<li><a href="https://github.com/ACE-Responder/RogueSliver" target="_blank">RogueSliver</a> - A suite of tools to disrupt campaigns using the Sliver C2 framework.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://pentests.nl/pentest-blog/cve-2023-28130-command-injection-in-check-point-gaia-portal/" target="_blank">CVE-2023-28130 - Command Injection in Check Point Gaia Portal</a>. Seems rough for a firewall vendor to get RCE'd. Again. At least its authenticated this time?</li>
<li><a href="https://github.com/iosifache/semgrep-rules-manager" target="_blank">semgrep-rules-manager</a> - Manager of third-party sources of Semgrep rules 🗂.</li>
<li><a href="https://github.com/b4rth0v5k1/Night_Walker" target="_blank">Night_Walker</a></li>
<li><a href="https://github.com/the-useless-one/pywerview" target="_blank">Pywerview</a> - A (partial) Python rewriting of PowerSploit's PowerView for when you’re proxing your traffic or operating from a linux device.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+1)</p>
<p>Blogs monitored: 354 (+1)</p>
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
