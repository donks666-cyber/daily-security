Title: Last Week in Security (LWiS) - 2025-12-15
Date: 2025-12-15 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-12-15
Author: Erik
Summary: Moonwalk++ stack telemetry bypass (<a href="https://x.com/klezVirus" target="_blank">@KlezVirus</a>), a pile of Mediatek CVEs (<a href="https://x.com/hyprdude" target="_blank">@hyprdude</a>), AppleScript decompiler (<a href="https://x.com/__pberba__" target="_blank">@__pberba__</a>), SCOM hacking (<a href="https://x.com/unsigned_sh0rt" target="_blank">@unsigned_sh0rt</a> + <a href="https://x.com/breakfix" target="_blank">@breakfix</a>), .NET SOAP disaster (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-12-08 to 2025-12-15.</p>
<aside class="m-block m-success">
<h3>Holiday Break</h3>
<p>LWiS will be off the next two weeks for the holidays. See you in 2026!</p>
</aside>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sharpen your Red Team skills with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p style="text-indent: 0;">Start your Red Team training with Altered Security! We offer affordable Red Team courses with enterprise-like hands-on labs and lifetime access to course materials.</p>
<p style="text-indent: 0;">Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Join more than 50,000 professionals from 130+ countries.</p>
<p style="text-indent: 0;">Get 20% OFF on all courses and instructor-led bootcamps to be held in Q1 and Q2 2026 in our Black Friday deals until December 17, 2025. No coupon code required. <strong><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://www.ic3.gov/PSA/2025/PSA251205" target="_blank">Criminals Using Altered Proof-of-Life Media to Extort Victims in Virtual Kidnapping for Ransom Scams</a> - It's <a href="https://www.reddit.com/r/StableDiffusion/comments/1pn9ygp/wan22_nano_banana_pro/" target="_blank">pretty remarkable</a> what self-hostable AI models can produce (Nano Banana Pro isn't self-hostable, but WAN2.2 is). It's time to set up a <a href="https://www.staysafeonline.org/campaigns/safeword" target="_blank">safe word</a> if you haven't already.</li>
<li><a href="https://www.hacklore.org/" target="_blank">Stop Hacklore!</a> - "Hacklore.org exists to separate myth from reality. Our goal is to help everyday people and small organizations focus on the simple, fact-based steps that truly protect their data and devices—keeping software up to date, using strong passwords and passkeys, using a password manager, and enabling multi-factor authentication." I hope we can stop mandatory password changes without evidence of a breach!</li>
<li><a href="https://lwn.net/Articles/1049831/" target="_blank">The (successful) end of the kernel Rust experiment</a> - "Rust in the kernel is no longer experimental — it is now a core part of the kernel and is here to stay." As <a href="https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html" target="_blank">Google has shown</a>, memory safe languages introduce far fewer memory safety bugs than C/C++.</li>
<li><a href="https://www.privacyguides.org/news/2025/12/10/atlanta-activist-charged-with-wiping-phone-before-cbp-search/" target="_blank">Atlanta activist charged with wiping phone before CBP search</a> - GrapheneOS has a "<a href="https://grapheneos.org/features#duress" target="_blank">Duress PIN</a>" feature that will wipe the device and eSIMs when entered. It would be interesting to know if Samuel entered the PIN himself or if a CBP agent did it after being told the PIN. The incident happened almost a year ago, but is just now going to court after an arrest on December 4th while being stopped over an issue with a vehicle tail light led to a grand jury indictment for the wiping of the phone a year ago.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2025/12/a-look-at-android-itw-dng-exploit.html" target="_blank">A look at an Android ITW DNG exploit</a> - Much like the <a href="https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html" target="_blank">iOS FORCEDENTRY exploits</a> this write up details a "zero click" image based exploit for Android. Looks like it was targeting WhatsApp users with Samsung phones. In this case the DNG image parser on Samsung phones specifically was able to be exploited to execute arbitrary code. Of note, memory tagging extensions (MTE) would have prevented this but are disabled by default on Samsung phones. iOS is not immune to this type of exploit, as the most recent iOS update 26.2 fixed a <a href="https://support.apple.com/en-us/125884" target="_blank">AppleJPEG</a> parsing vulnerability (as well as a few actively exploited WebKit vulnerabilities).</li>
<li><a href="https://klezvirus.github.io/posts/Moonwalk-plus-plus/" target="_blank">Malware Just Got Its Free Passes Back!</a> - SilentMoonwalk was a great advancement when it released, now Moonwalk++ (or is it --?) is here with some cleaver stack modification that uses "desync gadgets" instead of fixed registers or instruction sequences.</li>
<li><a href="https://horizon3.ai/attack-research/the-freepbx-rabbit-hole-cve-2025-66039-and-others/" target="_blank">The FreePBX Rabbit Hole: CVE-2025-66039 and others</a> - "The main pre-requisite for unauthenticated exploitation is having FreePBX configured with either “webserver” authentication type or no authentication at all." Not exploitable in the default configuration.</li>
<li><a href="https://blog.coffinsec.com/0days/2025/12/15/more-like-mediarekt-amirite.html" target="_blank">mediatek? more like media-rekt, amirite.</a> - 19+ vulnerabilities in Mediatek's MT76xx and MT7915 Wifi chipset family with PoCs for each. Bonus points of the ridiculous justification for severity ratings from Mediatek.</li>
<li><a href="https://pberba.github.io/security/2025/12/14/decompiling-run-only-applescripts/" target="_blank">Decompiling run-only AppleScripts</a> - Today I learned you can compile AppleScript.</li>
<li><a href="https://specterops.io/blog/2025/12/11/azure-seamless-sso-when-cookie-theft-doesnt-cut-it/" target="_blank">Azure Seamless SSO: When Cookie Theft Doesn’t Cut It</a> - Azure Seamless SSO allows users to sign in to apps using Azure AD, but get the actual Kerberos tickets from the on-premises domain controller. In this attack path a user's password is known, and using Azure Seamless SSO the attacker is able to bypass conditional access policies and take over the domain using Automation Runbooks.</li>
<li><a href="https://specterops.io/blog/2025/12/10/scommand-and-conquer-attacking-system-center-operations-manager-part-1/" target="_blank">SCOMmand and Conquer – Attacking System Center Operations Manager (Part 1)</a> - It turns out way more enterprises are using Microsoft's System Center Operations Manager (SCOM) than I thought, and Garrett Foster is here to use it to escalate privileges, harvest credentials, and compromise anything SCOM manages. Appreciate the shout out for <a href="https://ludus.cloud" target="_blank">Ludus</a> in the acknowledgements section!</li>
<li><a href="https://specterops.io/blog/2025/12/10/scommand-and-conquer-attacking-system-center-operations-manager-part-2/" target="_blank">SCOMmand And Conquer – Attacking System Center Operations Manager (Part 2)</a> - Matt Johnson digs deep into the client/server communication in Microsoft's System Center Operations Manager (SCOM) and ends up writing his own client to interact with SCOM, including the ability to decrypt stored credentials and policies. The domain used in the examples is the default <a href="https://ludus.cloud" target="_blank">Ludus</a> AD domain (ludus.domain) 😊.</li>
<li><a href="https://portswigger.net/research/the-fragile-lock" target="_blank">The Fragile Lock: Novel Bypasses For SAML Authentication</a> - Parser inconsistencies strike again resulting in a full authentication bypass in Ruby and PHP SAML implementations.</li>
<li><a href="https://trigger.dev/blog/shai-hulud-postmortem" target="_blank">How we got hit by Shai-Hulud: A complete post-mortem</a> - A look at how one company detected and responded to the latest JavaScript supply chain attack. Now consider if the attacker hadn't been so loud. How long could the attacker have persisted on the developer's machine? Notice the detection was due to GitHub noise, nothing from the endpoint...</li>
<li><a href="https://labs.watchtowr.com/soapwn-pwning-net-framework-applications-through-http-client-proxies-and-wsdl/" target="_blank">SOAPwn: Pwning .NET Framework Applications Through HTTP Client Proxies And WSDL</a> - The Simple Object Access Protocol (SOAP) has never been "simple." In fact, this blog comes with a <a href="https://watchtowr.com/wp-content/uploads/SOAPwnwatchtowr_soappwn-research-whitepaper_10-12-2025.pdf?ref=labs.watchtowr.com" target="_blank">[PDF] 92 page whitepaper</a>, and delivers some delicious pre-authentication remote code execution exploits. Microsoft not only refused to fix the underlying issue in .NET, but then refused to fix vulnerabilities that leverage the issue in their own applications!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/klezVirus/Moonwalk--" target="_blank">Moonwalk--</a> - Moonwalk++: Simple POC Combining StackMoonwalking and Memory Encryption.</li>
<li><a href="https://github.com/mellow-hype/mediarekt-2025" target="_blank">mediarekt-2025</a> - PoCs for Mediatek CVEs affecting MT7622/MT7915 and others.</li>
<li><a href="https://github.com/pberba/applescript-decompiler" target="_blank">applescript-decompiler</a> - A decompiler for run-only applescripts.</li>
<li><a href="https://github.com/breakfix/SharpSCOM" target="_blank">SharpSCOM</a> - A C# utility for interacting with SCOM.</li>
<li><a href="https://github.com/Offensium/SCOM-Deployment-with-Ansible-and-Terraform" target="_blank">SCOM-Deployment-with-Ansible-and-Terraform</a> - Easy to deploy SCOM setup that makes use of Terraform and Ansible. [If you're not using <a href="https://ludus.cloud" target="_blank">Ludus</a> and <a href="https://github.com/Synzack/ludus_scom" target="_blank">ludus_scom</a> for your lab]</li>
<li><a href="https://github.com/umpolungfish/byvalver" target="_blank">byvalver</a> - takes shellcode with null-bytes &amp; "denullifies" it.</li>
<li><a href="https://github.com/lsecqt/Find-AdminAccess" target="_blank">Find-AdminAccess</a> - This C# tool sprays for admin access over the entire domain.</li>
<li><a href="https://github.com/sailay1996/CVE-2025-53772" target="_blank">CVE-2025-53772</a> - POC for cve-2025-53772 a remote code execution vulnerability in Microsoft Web Deploy (msdeploy) caused by unsafe deserialization of HTTP header data.</li>
<li><a href="https://github.com/3lp4tr0n/SessionHop" target="_blank">SessionHop</a> - Windows Session Hijacking via COM.</li>
<li><a href="https://github.com/P0142/Lamperlv3" target="_blank">Lamperlv3</a> - Third iteration of Lamperl, a Linux agent for the Adaptix C2 being developed for a blog post.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/kiddo-pwn/CVE-2024-50629_50631" target="_blank">CVE-2024-50629_50631</a> - N-day Exploit for Synology BeeStation RCE by DEVCORE (Pwn2Own 2024).</li>
<li><a href="https://kiddo-pwn.github.io/blog/2025-11-30/writing-sync-popping-cron" target="_blank">Writing Sync, Popping Cron: DEVCORE's Synology BeeStation RCE &amp; A Novel SQLite Injection RCE Technique (CVE-2024-50629~50631)</a> - The SQLite injection to RCE is worth the read.</li>
<li><a href="https://maccarita.com/posts/idesaster/" target="_blank">IDEsaster: A Novel Vulnerability Class in AI IDEs</a> - "Over 30 separate security vulnerabilities identified and reported."</li>
<li><a href="https://github.com/mandiant/gostringungarbler" target="_blank">gostringungarbler</a> - Python tool to resolve all strings in Go binaries obfuscated by garble.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 493 (+2)</p>
<p>Blogs monitored: 438 (+2)</p>
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
