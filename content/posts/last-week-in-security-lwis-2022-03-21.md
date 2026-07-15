Title: Last Week in Security (LWiS) - 2022-03-21
Date: 2022-03-21 23:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-03-21
Author: Erik
Summary: Browser in the Browser (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), OSINT Map (<a href="https://twitter.com/MalfratsInd" target="_blank">@MalfratsInd</a>), Rust packer (<a href="https://twitter.com/verixvogel" target="_blank">@verixvogel</a>), local Kerberos to bypass UAC (<a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>), crash to read/write in Chakra (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), AtlasC2 (<a href="https://twitter.com/Gr1mmie" target="_blank">@Gr1mmie</a>), detecting Shadow Credentials (<a href="https://twitter.com/cfalta" target="_blank">@cfalta</a> ), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-03-14 to 2022-03-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.theverge.com/2022/3/15/22979251/microsoft-file-explorer-ads-windows-11-testing" target="_blank">Microsoft says Windows 11 File Explorer ads were ‘not intended to be published externally’</a>. Microsoft is slowly turning Windows into a "free to play" operating system. This started with ads in tiles in Windows 8.</li>
<li><a href="https://www.praetorian.com/blog/ides-of-march-chariots-launch-day/" target="_blank">Ides of March – Chariot’s Launch Day</a>. Praetorian launches their continous attack surface monitoring service which looks to be built on <a href="https://www.praetorian.com/blog/23-and-me-offensive-dna-and-nuclei-templates/" target="_blank">Nuclei Templates</a>.</li>
<li><a href="https://portswigger.net/daily-swig/npm-maintainer-targets-russian-users-with-data-wiping-protestware" target="_blank">NPM maintainer targets Russian users with data-wiping ‘protestware’</a>. Another reminder to check your dependency management solution.</li>
<li><a href="https://www.justice.gov/usao-sdny/pr/founder-cyberfraud-prevention-company-pleads-guilty-defrauding-investors-over-100" target="_blank">Founder Of Cyberfraud Prevention Company Pleads Guilty To Defrauding Investors Of Over $100 Million</a>. A lot of cybersecurity is snake oil, and this salesman got caught.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://mrd0x.com/browser-in-the-browser-phishing-attack/?no-cache=1" target="_blank">Browser In The Browser (BITB) Attack</a>. The creation of false windows inside of browser pages isn't exactly new (see <a href="https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/" target="_blank">The inception bar</a>) but this is the first time I've seen an fake SSO prompt window. Windows/macOS authentication prompts are also possible - check out <a href="https://twitter.com/fuzz_sh/status/1501364329593118726" target="_blank">@fuzz_sh</a>'s work.</li>
<li><a href="https://connormcgarr.github.io/type-confusion-part-2/" target="_blank">Exploit Development: Browser Exploitation on Windows - CVE-2019-0567, A Microsoft Edge Type Confusion Vulnerability (Part 2)</a>. Connor is back with part 2 which takes the exploit PoC from a simple crash to a read/write primitive and then to code execution against ChakraCore. ASLR, DEP, and CFG are all on the table as well, so this is an amazing bit of modern exploitation learning.</li>
<li><a href="https://www.exandroid.dev/2022/03/21/initial-access-right-to-left-override-t1036002/" target="_blank">Initial Access - Right-To-Left Override [T1036.002]</a>. Not a new technique, but susinctly presented with AV bypasses as well. Code <a href="https://github.com/ExAndroidDev/rtlo-attack" target="_blank">here</a>.</li>
<li><a href="https://www.x86matthew.com/view_post?id=notepadexec" target="_blank">NotepadExec - Using notepad.exe to launch an EXE without code injection</a>. Right click and "Open" an exe, but programatically.</li>
<li><a href="https://cyberstoph.org/posts/2022/03/detecting-shadow-credentials/" target="_blank">Detecting shadow credentials</a>. This post shows how defenders can look into msDS-KeyCredentialLink attributes and the flow to determine if they are legitimate or not.</li>
<li><a href="https://www.tiraniddo.dev/2022/03/bypassing-uac-in-most-complex-way.html" target="_blank">Bypassing UAC in the most Complex Way Possible!</a>. Local kerberos funny business with the service control manager on a domain joined machine to bypass UAC? <a href="https://gist.github.com/tyranid/c24cfd1bd141d14d4925043ee7e03c82" target="_blank">Intersting...</a></li>
<li><a href="https://claroty.com/2022/03/16/blog-research-arya-the-new-tailor-made-eicar-using-yara/" target="_blank">Arya: The New Tailor-Made EICAR Using Yara</a>. Get "malicious" files from yara rules. These can be the moder EICAR test files of modern purple teams.</li>
<li><a href="https://xz.aliyun.com/t/11041" target="_blank">CVE-2022-26500 Veeam Backup &amp; Replication RCE</a>. This is analysis and exploitaiton of the Veeam unauthenticated remote RCE from last week.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NtQuerySystemInformation/CustomKeyboardLayoutPersistence" target="_blank">CustomKeyboardLayoutPersistence</a> can achieve execution using a custom keyboard layout, tested in Windows 11 Home version 21H2. Warning: there is no code related to the uninstallation process in the PoC.</li>
<li><a href="https://github.com/Group3r/Group3r" target="_blank">Group3r</a> can find vulnerabilities in AD Group Policy, but do it better than Grouper2 did.</li>
<li><a href="https://map.malfrats.industries/" target="_blank">Malfrat's OSINT Map</a> is an update to the <cite>OSINT Framework &lt;https://osintframework.com/&gt;</cite>.  <a href="https://github.com/Malfrats/OSINT-Map" target="_blank">OSINT-Map</a> is the GitHub repo if you'd like to contribute.</li>
<li><a href="https://github.com/frank2/oxide" target="_blank">oxide</a> A PoC packer written in Rust!</li>
<li><a href="https://github.com/Gr1mmie/AtlasC2" target="_blank">AtlasC2</a> is a C# C2 Framework centered around Stage 1 operations.</li>
<li><a href="https://github.com/9rnt/poro" target="_blank">poro</a> is a tool to scan publicly accessible assets on your AWS cloud environment.</li>
<li><a href="https://github.com/breakpointHQ/snoop" target="_blank">snoop</a> Secretly record audio and video with chromium based browsers. Be sure to check out <a href="https://github.com/breakpointHQ/VOODOO/" target="_blank">VOODOO</a>, the macOS Man in the Browser Framework as well.</li>
<li><a href="https://github.com/Gr1mmie/Coeus" target="_blank">Coeus</a> is an ADSI based Situational Awareness toolkit for domain environments with modularity in mind. Allows for the enumeration of users/groups/computers as well as some common misconfigurations including roasting (AS-REP, kerber) and delegation (Constrained, Unconstrained, RCBD) attacks.</li>
<li><a href="https://github.com/xepor/xepor" target="_blank">xepor</a> is a web routing framework for reverse engineers and security researchers, brings the best of mitmproxy &amp; Flask.</li>
<li><a href="https://github.com/lab52io/LeakedHandlesFinder" target="_blank">LeakedHandlesFinder</a> is a leaked Windows processes handles identification tool. Useful for identify new LPE vulnerabilities during a pentest or simply as a new research process. Currently supports exploiting (autopwn) procesess leaked handles spawning a new arbitrary process (cmd.exe default).</li>
<li><a href="https://github.com/surajpkhetani/AutoSmuggle" target="_blank">AutoSmuggle</a> is a utility to craft HTML smuggled files for Red Team engagements.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/wumb0/rust_bof" target="_blank">rust_bof</a>. Cobalt Strike Beacon Object Files (BOFs) written in rust with rust core and alloc.</li>
<li><a href="https://github.com/V1D1AN/S1EM" target="_blank">S1EM</a>. This project is a SIEM with SIRP and Threat Intel, all in one.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 408 (+0)</p>
<p>Blogs monitored: 290 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
