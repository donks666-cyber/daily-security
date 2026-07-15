Title: Last Week in Security (LWiS) - 2023-09-11
Date: 2023-09-11 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-09-11
Author: Erik
Summary: Zero-click iOS exploits (<a href="https://twitter.com/citizenlab" target="_blank">@citizenlab</a>), in-the-wild Chrome 0day, physical/mobile RE writeup (<a href="https://twitter.com/elttam/" target="_blank">@elttam</a>), Linux LPE (<a href="https://twitter.com/SidewayRE" target="_blank">@SidewayRE</a>), Protected Process Dumper (<a href="https://twitter.com/tastypepperoni" target="_blank">@tastypepperoni</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-08-28 to 2023-09-11.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://tailscale.com/blog/mullvad-integration/" target="_blank">Mullvad on Tailscale: Privately browse the web</a> - In case the Tailscale/Mullvad fans missed it.</li>
<li><a href="https://blog.google/threat-analysis-group/active-north-korean-campaign-targeting-security-researchers/" target="_blank">Active North Korean campaign targeting security researchers</a> - Researchers have been and will always be a target. Share with those starting out in security research as well. You opened that project in a disposable VM, right?</li>
<li><a href="https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20video%20and%20slides/" target="_blank">DEF CON 31 recordings are out!</a> - In case you missed it.</li>
<li><a href="https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/" target="_blank">BLASTPASS NSO Group iPhone Zero-Click, Zero-Day Exploit Captured in the Wild</a>. Another zero click for iOS? Perhaps this prompted the new <a href="https://security.apple.com/research-device" target="_blank">Apple Security Research Device Program</a>.</li>
<li><a href="https://chromereleases.googleblog.com/2023/09/stable-channel-update-for-desktop_11.html" target="_blank">Google is aware that an exploit for CVE-2023-4863 exists in the wild.</a>. Not to be left out of the 0day fun, Chrome also got an update to in-the-wild 0day.</li>
<li><a href="https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/" target="_blank">Results of Major Technical Investigations for Storm-0558 Key Acquisition</a>. So a debug log contained the key due to a race condition, and it eventually got moved to a compromised machine (or so they think). Did the Storm-0558 actors get "lucky?" I suppose, but if you aren't waiting for a debug log containing the key by having compromised workstations, you won't get "lucky." And then to figure out how to use it to pillage emails from government customers... clearly this APT is serious.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2023/08/leveraging-vscode-extensions-for-initial-access/" target="_blank">Leveraging VSCode Extensions for Initial Access</a> - Targeting developers? Try this for initial access.</li>
<li><a href="https://tastypepperoni.medium.com/bypassing-defenders-lsass-dump-detection-and-ppl-protection-in-go-7dd85d9a32e6" target="_blank">Bypassing Defender's LSASS dump detection and PPL protection In Go</a> - A little PPL bypass with sysinternal drivers. Sysinternal drivers tend to flag against EDRs so test before use. Blog came with a <a href="https://github.com/tastypepperoni/PPLBlade" target="_blank">tool</a>.</li>
<li><a href="https://trufflesecurity.com/blog/4500-of-the-top-1-million-websites-leaked-source-code-secrets/" target="_blank">4,500 of the Top 1 Million Websites Leaked Source Code, Secrets</a> - Friendly reminder to include repos and source-code analysis in your recon workflow. Don't forget to try API keys even if they came from a previous commit, the developer may or may not have revoked those keys...</li>
<li><a href="https://www.synacktiv.com/publications/gpoddity-exploiting-active-directory-gpos-through-ntlm-relaying-and-more" target="_blank">GPOddity: exploiting Active Directory GPOs through NTLM relaying, and more!</a> - "A new versatile attack vector: spoofing GPO location through the gPCFileSysPath attribute." Check out the <a href="https://github.com/synacktiv/GPOddity" target="_blank">GPOddity</a> tool release as well.</li>
<li><a href="https://www.hexacorn.com/blog/2023/09/09/lolbins-for-connoisseurs-part-2/" target="_blank">Lolbins for connoisseurs… Part 2</a> - Follow up to <a href="https://www.hexacorn.com/blog/2023/08/25/lolbins-for-connoisseurs/" target="_blank">part 1</a>. Good reminder that LOLbins may be used by other third-part software. This could break basic detections.</li>
<li><a href="https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-2-obfuscation-masking" target="_blank">Revisiting the User-Defined Reflective Loader Part 2: Obfuscation and Masking</a> - "...introduced the User-Defined Reflective Loader Visual Studio (UDRL-VS) template"</li>
<li><a href="https://www.elttam.com/blog/re-of-lr3/" target="_blank">RE of LR3 - Peeking under the bonnet of the Litter Robot 3</a>. Great, in depth, physical and mobile app hacking.</li>
<li><a href="https://www.synacktiv.com/en/publications/old-bug-shallow-bug-exploiting-ubuntu-at-pwn2own-vancouver-2023" target="_blank">Old bug, shallow bug: Exploiting Ubuntu at Pwn2Own Vancouver 2023</a>. A great Linux LPE write up and exploit code as well. This is the first LPE I've seen written in Go!</li>
<li><a href="https://decoder.cloud/2023/09/05/from-ntauthcertificates-to-silver-certificate/" target="_blank">From NTAuthCertificates to “Silver” Certificate</a>. Some novel if not too sneaky persistence for a Windows domain.</li>
<li><a href="https://posts.specterops.io/shadow-wizard-registry-gang-structured-registry-querying-9a2fab62a26f" target="_blank">Shadow Wizard Registry Gang: Structured Registry Querying</a>. Full steam ahead with the structured data train. Really excited to watch (and help?) <a href="https://github.com/SpecterOps/Nemesis" target="_blank">Nemesis</a> expand. The day tools adapt to it as the industry standard we'll know it has won.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/nyxgeek/guestlist/" target="_blank">guestlist</a> - Labor day release from a <a href="https://github.com/nyxgeek/track_the_planet/tree/main" target="_blank">DEF CON 31 talk</a>. A tool for identifying guest relationships between companies.</li>
<li><a href="https://github.com/whokilleddb/ETWListicle" target="_blank">ETWListicle</a> -  List the ETW provider(s) in the registration table of a process.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2451" target="_blank">Issue 2451: Windows: System Drive Replacement During Impersonation EoP</a>. Windows LPE patched 2023-08-14 with PoC.</li>
<li><a href="https://blog.doyensec.com//2023/08/31/introducing-session-hijacking-visual-exploitation.html" target="_blank">Introducing Session Hijacking Visual Exploitation (SHVE): An Innovative Open-Source Tool for XSS Exploitation</a>. This is the coolest browser tool since the OG <a href="https://github.com/beefproject/beef" target="_blank">beef</a> and <a href="https://shadow-workers.github.io/" target="_blank">Shadow Workers</a>.</li>
<li><a href="https://redhuntlabs.com/blog/introducing-a-free-attack-surface-recon-api-by-redhunt-labs/" target="_blank">Introducing Free Attack Surface Recon API by RedHunt Labs</a>. Limited for now but free!</li>
<li><a href="https://github.com/mitre/caldera-ot" target="_blank">caldera-ot</a> - Caldera OT Plugin &amp; Capabilities.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/CyberCX-STA/PurpleOps" target="_blank">PurpleOps</a> - An open-source self-hosted purple team management web application.</li>
<li><a href="https://github.com/20urc3/Sekiryu" target="_blank">Sekiryu</a> - Comprehensive toolkit for Ghidra headless.</li>
<li><a href="https://github.com/nickvourd/Supernova" target="_blank">Supernova</a> - Real shellcode encryption tool.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 354 (+0)</p>
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
