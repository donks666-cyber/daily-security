Title: Last Week in Security (LWiS) - 2022-10-24
Date: 2022-10-24 17:13
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-10-24
Author: Erik
Summary: Untangling Azure Permissions (<a href="https://twitter.com/0xcsandker" target="_blank">@0xcsandker</a>), V8 and JS internals of Chrome (<a href="https://twitter.com/jack_halon" target="_blank">@jack_halon</a>), MS Office Online Server RCE chain (<a href="https://twitter.com/IndiShell1046" target="_blank">@IndiShell1046</a>), ManageEngine Decryptor (<a href="https://twitter.com/W9HAX" target="_blank">@W9HAX</a>), SharedMemUtils (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-10-17 to 2022-10-24.</p>
<p>This week I reviewed 372 blog posts and 2144 tweets to find only the best and most relevant items to include here.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/" target="_blank">Investigation Regarding Misconfigured Microsoft Storage Location</a>. SOCRadar put Microsoft on blast with their post <a href="https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/" target="_blank">Sensitive Data of 65,000+ Entities in 111 Countries Leaked due to a Single Misconfigured Data Bucket</a>. 6 Azure buckets holding some sensitive items like statements of work were misconfigured and publicly accessible.</li>
<li><a href="https://posts.specterops.io/ghostwriter-v3-1-now-available-47cfcccd6b02" target="_blank">Ghostwriter v3.1 Now Available</a>. Now with deconfliction support!</li>
<li><a href="https://www.forbes.com/sites/emilybaker-white/2022/10/20/tiktok-bytedance-surveillance-american-user-data/" target="_blank">TikTok Parent ByteDance Planned To Use TikTok To Monitor The Physical Location Of Specific American Citizens</a>. Is anyone surprised?</li>
<li><a href="https://www.securityweek.com/ida-pro-owner-hex-rays-acquired-european-vc-firm" target="_blank">IDA Pro Owner Hex-Rays Acquired by European VC Firm</a>. With more competition VC firms are getting into the game.</li>
<li><a href="https://www.reuters.com/world/middle-east/irans-atomic-energy-organization-says-e-mail-was-hacked-state-media-says-2022-10-23/" target="_blank">Iran's atomic energy organization says e-mail was hacked</a>. I think "has been hacked by multiple parties" would probably be more accurate here...</li>
<li><a href="https://githubcopilotinvestigation.com/#help-us-investigate" target="_blank">GitHub Copilot investigation</a>. Surely the Microsoft lawyers signed off on Copilot?</li>
<li><a href="https://www.youtube.com/user/DEFCONConference/videos" target="_blank">DEF CON 30 Videos Released</a>. Enjoy!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html" target="_blank">Legitimate Rats: A Comprehensive Forensic Analysis of the Usual Suspects</a>. Good to see people taking <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a> seriously.</li>
<li><a href="https://blog.fox-it.com/2022/10/18/im-in-your-hypervisor-collecting-your-evidence/" target="_blank">I'm in your hypervisor, collecting your evidence</a>. Fox-IT adds ESXi live acquisition to its <a href="https://github.com/fox-it/dissect" target="_blank">dissect</a> tool suite.</li>
<li><a href="https://jhalon.github.io/chrome-browser-exploitation-1/" target="_blank">Chrome Browser Exploitation, Part 1: Introduction to V8 and JavaScript Internals</a>. Most people use their OS as a loader for Chrome, so Chrome has become a target for all kinds of adversaries. However, actually understanding and exploiting Chrome is very difficult. This intro post shows some of the complexity involved.</li>
<li><a href="https://www.mdsec.co.uk/2022/10/microsoft-office-online-server-remote-code-execution/" target="_blank">Microsoft Office Online Server Remote Code Execution</a>. Web based authentication coercion that Microsoft claims it's a feature!</li>
<li><a href="https://www.synacktiv.com/en/publications/php-filters-chain-what-is-it-and-how-to-use-it.html" target="_blank">PHP Filters Chain: What Is It and How to Use It</a>. "Searching for new gadget chains to exploit deserialization vulnerabilities can be tedious. In this article we will explain how to combine a recently discovered technique called PHP filters [LOKNOP-GIST], to transform file inclusion primitives in PHP applications to remote code execution. To support our explanations we will rely on a Laravel file inclusion gadget chains that was discovered during this research."</li>
<li><a href="https://www.trustedsec.com/blog/the-curious-case-of-the-password-database/" target="_blank">The Curious Case of the Password Database</a>. Yes, passwords can be encrypted by a product, but unless they require user input to decrypt passwords there must be a way the software decrypts them. I've seen this is multiple products so Manage Engine is not unique. It's usually just a mater of finding the static key and encryption parameters.</li>
<li><a href="https://www.trustedsec.com/blog/dameware-mini-the-sleeper-hit-of-2019/" target="_blank">Dameware Mini: The Sleeper Hit of 2019?</a>. More traitorware!</li>
<li><a href="https://www.x86matthew.com/view_post?id=shared_mem_utils" target="_blank">SharedMemUtils - A simple tool to automatically find vulnerabilities in shared memory objects</a>. Sometimes you can write to shared memory objects of high-privileged services on Windows. A fun primitive to explore potential privescs.</li>
<li><a href="https://labs.withsecure.com/advisories/microsoft-office-365-message-encryption-insecure-mode-of-operation" target="_blank">Microsoft Office 365 Message Encryption Insecure Mode of Operation</a>. ECB mode, not even once.</li>
<li><a href="https://github.com/chainguard-dev/osquery-defense-kit" target="_blank">osquery-defense-kit</a> - Production-ready detection &amp; response queries for osquery.</li>
<li><a href="https://blog.offensive.af/changing-memory-protection-using-apc" target="_blank">Changing memory protection using APC</a>. Not brand new, but a deeper drive into it.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/csandker/Azure-AccessPermissions" target="_blank">Azure-AccessPermissions</a> - Easy to use PowerShell script to enumerate access permissions in an Azure Active Directory environment. Check out <a href="https://csandker.io//2022/10/19/Untangling-Azure-Permissions.html" target="_blank">the blog post</a> for details.</li>
<li><a href="https://github.com/fin3ss3g0d/cypherhound" target="_blank">cypherhound</a> - Python3 terminal application that contains 200+ Neo4j cyphers for BloodHound data sets</li>
<li><a href="https://github.com/CodeXTF2/ScreenshotBOF" target="_blank">ScreenshotBOF</a> - An alternative screenshot capability for Cobalt Strike that uses WinAPI and does not perform a fork &amp; run. Screenshot saved to disk as a file.</li>
<li><a href="https://github.com/bugch3ck/SharpEfsPotato" target="_blank">SharpEfsPotato</a> - Local privilege escalation from SeImpersonatePrivilege using EfsRpc.</li>
<li><a href="https://github.com/D1rkMtr/PatchThatAMSI" target="_blank">PatchThatAMSI</a> - This repo contains 6 AMSI patches, both force the triggering of a conditional jump inside AmsiOpenSession() that close the Amsi scanning session. The 1st patch by corrupting the Amsi context header and the 2nd patch by changing the string "AMSI" that will be compared to the Amsi context header to "D1RK". The other just set ZF to 1.</li>
<li><a href="https://github.com/cisagov/ScubaGear" target="_blank">ScubaGear</a> - Automation to assess the state of your M365 tenant against CISA's baselines.</li>
<li><a href="https://github.com/zimawhit3/Bitmancer" target="_blank">Bitmancer</a> - Nim Library for Offensive Security Development.</li>
<li><a href="https://github.com/n00py/GetFGPP" target="_blank">GetFGPP</a> - Get Fine Grained Password Policy.</li>
<li><a href="https://github.com/marakew/syser" target="_blank">syser</a> - syser debugger x32/x64 ring3 with source level debugging/watch view/struct view.</li>
<li><a href="https://github.com/mickael-kerjean/webpty" target="_blank">webpty</a> - A secure webshell. Built for legitimate access, I could see it adopted for red team uses.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Linen-dev/linen.dev" target="_blank">linen.dev</a> - Google-searchable Slack alternative for Communities.</li>
<li><a href="https://github.com/cea-sec/usbsas" target="_blank">usbsas</a> - Tool and framework for securely reading untrusted USB mass storage devices.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 327 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
