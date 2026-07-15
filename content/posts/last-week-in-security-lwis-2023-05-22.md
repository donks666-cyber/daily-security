Title: Last Week in Security (LWiS) - 2023-05-22
Date: 2023-05-22 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-05-22
Author: Erik
Summary: From DA to EA (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), CS OPSEC (<a href="https://twitter.com/joehowwolf" target="_blank">@joehowwolf</a>), CS BOFs in BRC4 (<a href="https://twitter.com/NVISOsecurity" target="_blank">@NVISOsecurity</a>), Avast LPE (<a href="https://twitter.com/Denis_Skvortcov" target="_blank">@Denis_Skvortcov</a>), LOLBINs in AV (<a href="https://twitter.com/nas_bench" target="_blank">@nas_bench</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-05-09 to 2023-05-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.cloudflare.com/developer-week-2023-wrap-up/" target="_blank">Recapping Developer Week</a>. Cloudflare continues to release new products and make (good) changes to existing products. And yes, they did release an AI product.</li>
<li><a href="https://maia.crimew.gay/posts/optimeyes-leak/" target="_blank">infosec company owned completely by 4chan user</a>. Ouch.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-zip-domains-spark-debate-among-cybersecurity-experts/" target="_blank">New ZIP domains spark debate among cybersecurity experts</a>. I don't think there is debate, I think there are people claiming .zip will be a threat, but the only case I can see that being true is with programs that have interpreted .zip as a file since forever and may be fooled now that it can resolve as a URL. The "it looks like a file" argument strikes me as silly, since the anchor tag has been used to "disguise" URLs since the existence of the HTML standard. Oh look here's one now: <a href="https://example.com" target="_blank">legit.zip</a></li>
<li><a href="https://arstechnica.com/information-technology/2023/05/microsoft-patches-secure-boot-flaw-but-wont-enable-fix-by-default-until-early-2024/" target="_blank">Microsoft will take nearly a year to finish patching new 0-day Secure Boot bug</a>. Is this the first case of a disabled by default mitigation being shipped in response to an active, in the wild exploit?</li>
<li><a href="https://github.com/ChromeDevTools/rfcs/discussions/4" target="_blank">RFC: Override HTTP response headers locally with DevTools</a>. Now one of the most common use cases for Burp Suite is part of Chrome! For how see: <a href="https://tweak-extension.com/blog/how-to-override-response-headers-chrome" target="_blank">How to Override Response Headers with Chrome DevTools</a>.</li>
<li><a href="https://www.reddit.com/r/Defcon/comments/13m7qts/def_con_31_badge_update_sao_support/" target="_blank">DEF CON 31 Badge Update - SAO support!</a>. This year's DEF CON badges will support an add on "thing" shaped like a cyber punk wedge.</li>
<li><a href="https://medium.com/@cy1337/first-look-ghidras-10-3-emulator-7f74dd55e12d" target="_blank">First Look: Ghidra 10.3 Emulator</a>. Everyone is pumped about native dark mode, but the emulator is pretty sweet.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/from-da-to-ea-with-esc5-f9f045aa105c" target="_blank">From DA to EA with ESC5</a>. "There's a new, practical way to escalate from Domain Admin to Enterprise Admin." Sign me up. Another banger from Andy Robbins.</li>
<li><a href="https://posts.specterops.io/c2-and-the-docker-dance-mythic-3-0s-marvelous-microservice-moves-f6e6e91356e2" target="_blank">C2 and the Docker Dance: Mythic 3.0's Marvelous Microservice Moves</a>. I can't say I <strong>love</strong> the extreme microservice-y architecture of Mythic, but it's the easiest open source C2 to write a totally custom agent for at this point. Perhaps SpecterOps can use some of that <a href="https://specterops.io/news/specterops-raises-25m-to-accelerate-company-growth-and-expand-attack-path-management-solutions/" target="_blank">Series A</a> to contract a web UI pro to help with the front end. I say this out of love, as I actually use Mythic C2 for production operations.</li>
<li><a href="https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr-again" target="_blank">The printer goes brrrrr, again!</a>. 2 bytes is all it takes to RCE a Cannon printer.</li>
<li><a href="https://www.mdsec.co.uk/2023/05/nighthawk-0-2-4-taking-out-the-trash/" target="_blank">Nighthawk 0.2.4 - Taking Out The Trash</a>. The new version supports .NET memory sleep encryption, using a custom allocator to protect and encrypt not only the executed .NET assembly but also any of its allocations during runtime. It also adds reverse port forwards, improvements to hidden desktop, "extra life" exception hooking, and other minor improvements.</li>
<li><a href="https://www.elttam.com/blog/pwnassistant/" target="_blank">PwnAssistant - Controlling /home's via a Home Assistant RCE</a>. Awesome write up from recon to RCE against the popular home automation software.</li>
<li><a href="https://blog.assetnote.io/2023/05/10/sitecore-round-two/" target="_blank">Bypass IIS Authorisation with this One Weird Trick - Three RCEs and Two Auth Bypasses in Sitecore 9.3</a>. Another recon to RCE web app hacking write up.</li>
<li><a href="https://palant.info/2023/05/16/malicious-code-in-pdf-toolbox-extension/" target="_blank">Malicious code in PDF Toolbox extension</a>. Browsers are the new OS, but there is zero visibility or "anti-virus" for them. It's like the Windows 98 wild west days.</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-and-yara-can-i-have-your-signature/" target="_blank">Cobalt Strike and YARA: Can I Have Your Signature?</a>. Probably the best article on Cobalt Strike OPSEC that exists. Advanced teams have known about the satic loader signatures and other things for a while, but this post spells it all out and even gives examples of how to get around static detections. We're at a point where to be truly successful as an adversary you need to know assembly pretty well. Seems like the offensive security community has made the defenses better and raised the barrier to entry. Almost like the goal was to... @ImposeCost...</li>
<li><a href="https://dr4k0nia.github.io/posts/NixImports-a-NET-loader-using-HInvoke/" target="_blank">NixImports a .NET loader using HInvoke</a>. API Hashing in C# makes the dnSpy output a mess. Neat loader!</li>
<li><a href="https://danrevah.github.io/2023/05/15/CVE-2023-26818-Bypass-TCC-with-Telegram/" target="_blank">CVE-2023-26818 - Bypass TCC with Telegram in macOS</a>. While this is a write up on dylib injection in Telegram, many apps are vulnerable to a similar technique, especially third party apps.</li>
<li><a href="https://blog.nviso.eu/2023/05/15/introducing-cs2br-pt-i-how-we-enabled-brute-ratel-badgers-to-run-cobalt-strike-bofs/" target="_blank">Introducing CS2BR pt. I - How we enabled Brute Ratel Badgers to run Cobalt Strike BOFs</a>. If you've used BRC4 you know the pain of BOF conversion. Nviso teases a tool to automate it, hopefully it's released soon!</li>
<li><a href="https://blog.stratumsecurity.com/2023/05/16/sqli-waf-detection-bypass-techniques-that-still-work-in-2023/" target="_blank">SQLi - WAF Detection &amp; Bypass Techniques That Still Work in 2023</a>. For the web app assessors out there.</li>
<li><a href="https://the-deniss.github.io/posts/avast-privileged-arbitrary-file-create-on-restore/" target="_blank">Avast Anti-Virus privileged arbitrary file create on virus restore (CVE-2023-1586)</a>. More Avast privescs!</li>
<li><a href="https://neodyme.io/blog/csgo_from_zero_to_0day/" target="_blank">CS:GO: From Zero to 0-day</a>. Sure it's a video game exploit, but the writeup is top tier.</li>
<li><a href="https://www.trustedsec.com/blog/walking-the-tightrope-maximizing-information-gathering-while-avoiding-detection-for-red-teams/" target="_blank">Walking the Tightrope: Maximizing Information Gathering while Avoiding Detection for Red Teams</a>. Finally, a blog on red teaming, not just penetration testing! For anyone looking to get into adversary simulation, this is a good intro.</li>
<li><a href="https://sternumiot.com/iot-blog/mini-smart-plug-v2-vulnerability-buffer-overflow/" target="_blank">FriendlyName Buffer Overflow Vulnerability in Wemo Smart Plug V2</a>. Some solid hardware hacking.</li>
<li><a href="https://nasbench.medium.com/lolbined-finding-lolbins-in-av-uninstallers-bf29427d3cd8" target="_blank">LOLBINed — Finding “LOLBINs” In AV Uninstallers</a>. AV makes the best <a href="https://www.youtube.com/watch?v=9qM2m1LZuVo" target="_blank">traitorware</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/SadProcessor/CypherDog" target="_blank">CypherDog</a> - PoSh BloodHound Dog Whisperer.</li>
<li><a href="https://github.com/google/buzzer" target="_blank">buzzer</a> is a fuzzer toolchain that allows to write eBPF fuzzing strategies.</li>
<li><a href="https://github.com/vdohney/keepass-password-dumper" target="_blank">keepass-password-dumper</a> - Original PoC for CVE-2023-32784 (keepass master password disclosure).</li>
<li><a href="https://github.com/trustedsec/PPLFaultDumpBOF" target="_blank">PPLFaultDumpBOF</a> - Takes the original PPLFault and the original included DumpShellcode and combines it all into a BOF targeting cobalt strike.</li>
<li><a href="https://github.com/rasta-mouse/PPEnum" target="_blank">PPEnum</a> - Simple BOF to read the protection level of a process.</li>
<li><a href="https://github.com/grimlockx/ADCSKiller" target="_blank">ADCSKiller</a> - An ADCS Exploitation Automation Tool Weaponizing Certipy and Coercer.</li>
<li><a href="https://github.com/georgesotiriadis/Chimera" target="_blank">Chimera</a> - Automated DLL Sideloading Tool With EDR Evasion Capabilities.</li>
<li><a href="https://github.com/magisterquis/chromecookiestealer" target="_blank">chromecookiestealer</a> - Steal/Inject Chrome cookies over the DevTools (--remote-debugging-port) protocol.</li>
<li><a href="https://github.com/cedowens/GoBelt" target="_blank">GoBelt</a> - Golang programmatically invoking the SwiftBelt-JXA macOS system enumerator project (Golang running SwiftBelt-JXA via cgo).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dobin/avred" target="_blank">avred</a> - Analyse your malware to chirurgicaly obfuscate it.</li>
<li><a href="https://github.com/SySS-Research/smbcrawler" target="_blank">smbcrawler</a> is no-nonsense tool that takes credentials and a list of hosts and 'crawls' (or 'spiders') through those shares.</li>
<li><a href="https://github.com/Yunlongs/Goshawk" target="_blank">Goshawk</a> is a static analyze tool to detect memory corruption bugs in C source codes. It utilizes NLP to infer custom memory management functions and uses data flow analysis to abstract their behaviors and then adopts these summaries to enhance bug detection.</li>
<li><a href="https://github.com/mrexodia/dumpulator" target="_blank">dumpulator</a> - An easy-to-use library for emulating memory dumps. Useful for malware analysis (config extraction, unpacking) and dynamic analysis in general (sandboxing).</li>
<li><a href="https://github.com/saw-your-packet/EC2StepShell" target="_blank">EC2StepShell</a> is an AWS post-exploitation tool for getting high privileges reverse shells in public or private EC2 instances. It works by sending commands to EC2 instances using ssm:SendCommand and then retrieves the output using ssm:ListCommandInvocations or ssm:GetCommandInvocation.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 344 (+3)</p>
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
