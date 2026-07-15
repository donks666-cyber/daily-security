Title: Last Week in Security (LWiS) - 2021-08-23
Date: 2021-08-23 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-08-23
Author: Erik
Summary: iOS CSAM fallout, JS surveillance framework (<a href="https://twitter.com/imp0rtp3" target="_blank">@imp0rtp3</a> + <a href="https://twitter.com/felixaime" target="_blank">@felixaime</a>), 1Password dumper (<a href="https://twitter.com/djhohnstein" target="_blank">@djhohnstein</a>), Windows user behavior (<a href="https://twitter.com/Oddvarmoe" target="_blank">@Oddvarmoe</a>), BOF dev walkthrough (<a href="https://twitter.com/0xBoku" target="_blank">@0xBoku</a>), support opensource (<a href="https://twitter.com/porchetta_ind" target="_blank">@porchetta_ind</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-08-16 to 2021-08-23.</p>
<aside class="m-note m-warning">
<h3>A week off</h3>
<p>There will be no Last Week in Security next week (2021-08-30). It will return 2021-09-06.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><dl>
<dt>Apple CSAM fallout:</dt>
<dd><ul>
<li><a href="https://www.washingtonpost.com/opinions/2021/08/19/apple-csam-abuse-encryption-security-privacy-dangerous/" target="_blank">Opinion: We built a system like Apple’s to flag child sexual abuse material — and concluded the tech was dangerous</a>. A group from Princeton built a similar system to what Apple has deployed and decided it was too dangerous to put into practice. "Apple is gambling with security, privacy and free speech worldwide."</li>
<li><a href="https://github.com/AsuharietYgvar/AppleNeuralHash2ONNX/issues/1" target="_blank">Working Collision? #1</a>. This was the start of the collisions but it quickly snowballed.</li>
<li><a href="https://github.com/anishathalye/neural-hash-collider" target="_blank">neural-hash-collider</a> can generate collisions on demand.</li>
<li>Had enough of Apple? Look into <a href="https://grapheneos.org/" target="_blank">GrapheneOS</a>, <a href="https://calyxos.org/" target="_blank">CalyxOS</a>, or even a <a href="https://www.pine64.org/pinephone/" target="_blank">PinePhone</a>.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.macrumors.com/2021/08/17/apple-appeals-corellium-copyright-lawsuit/" target="_blank">Apple Appeals Corellium Copyright Lawsuit Loss After Settling Other Claims</a>. Last week the news section had a good news story about Apple dropping a case against Corellium. They've appealed the other case they lost. All this while claiming security researchers would be a check against CSAM scanning abuse...</li>
<li><a href="https://www.vice.com/en/article/n7bmxd/poly-network-hacker-returned-stolen-funds" target="_blank">A Hacker Stole and Then Returned $600 Million</a>. The wild west of finance sees it's largets heist yet (yes, bigger than <a href="https://en.wikipedia.org/wiki/Mt._Gox#Bankruptcy;_stolen_bitcoin_(2014%E2%80%93present)" target="_blank">Mt. Gox</a>). For technical details (facepalm warning) check out <a href="https://rekt.news/polynetwork-rekt/" target="_blank">rekt</a>.</li>
<li><a href="https://www.theverge.com/2021/8/19/22632888/microsoft-office-365-price-increase-march-2022" target="_blank">Microsoft announces price increase for Office 365 and Microsoft 365</a>. E5 is still crazy expensive.</li>
<li><a href="https://porchetta.industries/" target="_blank">Porchetta Industries Launches</a>. "The Information Security Industry doesn't have a direct way to support Offensive &amp; Defensive Open Source Security Tool developers even though it relies on them for a large portion of their services and/or internal capabilities. We're here to change that. Porchetta Industries provides a centralized platform for organizations to fund and support Open Source Security Tools."</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://posts.specterops.io/1password-secret-retrieval-methodology-and-implementation-6a9db3f3c709" target="_blank">1Password Secret Retrieval — Methodology and Implementation</a>. Password managers are a juicy target for post-exploitation. This post explores the 1password password manager and offers some detection tips. If an attacker is injecting code into processes undetected, it might be too late. Check out <a href="https://github.com/djhohnstein/1PasswordSuite" target="_blank">1PasswordSuite</a> for the tools.</li>
<li><a href="https://halove23.blogspot.com/2021/08/executing-code-in-context-of-trusted.html" target="_blank">Executing Code In Context Of A Trusted Agent (Part 1) - Windows Defender Antivirus</a>. The only thing better than bypassing AV is running in the context of AV itself. PoC <a href="https://github.com/klinix5/WinDefendInjectPoC" target="_blank">here</a>.</li>
<li><a href="https://www.praetorian.com/blog/introducing-gokart/" target="_blank">Introducing GoKart, a Smarter Go Security Scanner</a>. If you've got some Go code to review or are trying to exploit, give <a href="https://github.com/praetorian-inc/gokart" target="_blank">gokart</a> a shot.</li>
<li><a href="https://pentestlab.blog/2021/08/17/domain-escalation-printnightmare/" target="_blank">Domain Escalation – PrintNightmare</a>. Need a refresher or reference on all the PrintNighmare madness? This post covers remote discovery and exploitation.</li>
<li><a href="https://imp0rtp3.wordpress.com/2021/08/12/tetris/" target="_blank">Uncovering Tetris – a Full Surveillance Kit Running in your Browser</a>. A watering hole attack used JSON Hijacking and other methods to attempt to identify users. It even attempted to steal secrets from the user's local machine using websockets!</li>
<li><a href="https://www.trustedsec.com/blog/oh-behave-figuring-out-user-behavior/" target="_blank">Oh, Behave! Figuring Out User Behavior</a>. Once you gain access to a target workstation, how do you determine what the user does day to day? Which applications would be best to backdoor for persistence? This post explores some ways to answer these questions.</li>
<li><a href="https://o365blog.com/post/hybridhealthagent/" target="_blank">Spoofing Azure AD sign-ins logs by imitating AD FS Hybrid Health Agent</a>. If you have local admin you can export the AD FS Hybrid Health Agent secret and spam the Azure AD sign-in logs with fake entries.</li>
<li><a href="https://0xboku.com/2021/08/19/Bof-WhereAmI.html" target="_blank">Creating the WhereAmI Cobalt Strike BOF</a>. Bobby has been on a roll, churning out BOFs at a rapid pace. It likely took significant extra time to document and write up the process behind <a href="https://github.com/boku7/whereami" target="_blank">whereami</a> which dumps the environment variables without calling the WinAPI, and for that I am grateful!</li>
<li><a href="https://g-laurent.blogspot.com/2021/08/responders-dhcp-poisoner.html" target="_blank">Responder's DHCP Poisoner</a>. Responder 3.0.7.0 comes with a new DHCP module! Learn about it in this post.</li>
<li><a href="https://www.pwndefend.com/2021/08/22/razer-privilege-escalation-vulnerability/" target="_blank">Razer Windows LPE</a>. Simply attaching a Razer mouse (or a <a href="https://gist.github.com/tothi/3cdec3aca80e08a406afe695d5448936" target="_blank">spoofed</a> one) will run a UI as SYSTEM that you can use to open a file dialog and spawn a prompt with. I don't believe this has been weaponized without physical access or desktop interaction yet.</li>
<li><a href="https://medium.com/tenable-techblog/integer-overflow-to-rce-manageengine-asset-explorer-agent-cve-2021-20082-7e54cb2caad5" target="_blank">Integer Overflow to RCE — ManageEngine Asset Explorer Agent (CVE-2021–20082)</a>. This is a great in-depth post on the productization of an integer overflow into RCE.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/CCob/SweetPotato/pull/7" target="_blank">Added EfsRpc method (aka PetitPotam)</a>. SweetPotato gets a PetitPotam upgrade so if you have SeImpersonatePrivilege on a fully patched windows 10 machine, you can get SYSTEM.</li>
<li><a href="https://github.com/netero1010/ServiceMove-BOF" target="_blank">ServiceMove-BOF</a> is a new lateral movement technique by abusing Windows Perception Simulation Service to achieve DLL hijacking code execution. Note that is work on Windows 10 1809 or above only.</li>
<li><a href="https://github.com/alfarom256/BOF-ForeignLsass" target="_blank">BOF-ForeignLsass</a> dumps lsass memory by opening a handle to a process that already has a handle open to lsass, with the hopes of looking less suspicious by stealing this "legitimate" handle.</li>
<li><a href="https://github.com/armosec/kubescape" target="_blank">kubescape</a> is the first tool for testing if Kubernetes is deployed securely as defined in Kubernetes Hardening Guidance by to <a href="https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2716980/nsa-cisa-release-kubernetes-hardening-guidance/" target="_blank">NSA and CISA</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/optiv/Microsoft365_devicePhish" target="_blank">Microsoft365_devicePhish</a> is a a proof-of-concept script to conduct a phishing attack abusing Microsoft 365 OAuth Authorization Flow. Compare to <a href="https://github.com/AlteredSecurity/365-Stealer" target="_blank">365-Stealer</a> and <a href="https://github.com/rvrsh3ll/TokenTactics" target="_blank">TokenTactics</a>.</li>
<li><a href="https://github.com/secdev-01/Mimikore" target="_blank">Mimikore</a> is a .NET 5 single file application loader for Mimikatz or any Base64 PE.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
