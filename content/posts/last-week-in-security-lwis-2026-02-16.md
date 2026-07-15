Title: Last Week in Security (LWiS) - 2026-02-16
Date: 2026-02-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-02-16
Author: Erik
Summary: SharePoint enumeration (<a href="https://x.com/matthiasdeeg" target="_blank">@matthiasdeeg</a>), LNK "0days" (<a href="https://x.com/Wietze" target="_blank">@Wietze</a>), AMD driver LPE (<a href="https://x.com/Bad_Jubies" target="_blank">@Bad_Jubies</a>), POSTing to superadmin (<a href="https://x.com/XeEaton" target="_blank">@XeEaton</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-02-09 to 2026-02-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2026/01/android-theft-protection-feature-updates.html" target="_blank">New Android Theft Protection Feature Updates: Smarter, Stronger</a> - New improvements to anti-theft including detecting if a phone has been grabbed while unlocked as part of a "snatch-and-run." I've witnessed two "roadmen" on ebikes snatch a phone from someone's hands on the sidewalk in London. It's gotten so bad there is a <a href="https://www.currysplc.com/news-media/stories-insights/2025/mind-the-grab-our-campaign-to-raise-awareness-of-street-phone-theft/" target="_blank">Mind the Grab</a> campaign on the sidewalks.</li>
<li><a href="https://www.nysenate.gov/legislation/bills/2025/S9005" target="_blank">Senate Bill S9005</a> - The US state of New York is considering requiring every 3D printer sold in the state to be "capable of ensuring a three-dimensional printer will not proceed to print any print job unless the underlying three-dimensional printing file has been evaluated by a firearms blueprint detection algorithm and determined not to be a printing file that would produce a firearm or illegal firearm parts." Besides the impossibility of a "firearms blueprint detection algorithm," when did legislating the tool become the solution? Is New York also going to do the same for lathes, table saws, or injection molds?</li>
<li><a href="https://support.apple.com/en-us/126346" target="_blank">About the security content of iOS 26.3 and iPadOS 26.3</a> - <cite>dyld</cite> is the one to read: "Impact: An attacker with memory write capability may be able to execute arbitrary code. Apple is aware of a report that this issue may have been exploited in an extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 26. CVE-2025-14174 and CVE-2025-43529 were also issued in response to this report." Reported by Google's Threat Analysis Group (TAG); sounds like they found a whole exploit chain in the wild. Great work TAG! Update those iPhones and Macs.</li>
<li><a href="https://www.wiz.io/cyber-model-arena" target="_blank">Cyber Model Arena</a> - A new benchmark with deterministic scoring (vs LLM-as-a-judge).</li>
<li><a href="https://ahmedeldin.substack.com/p/the-israeli-spyware-firm-that-accidentally" target="_blank">The Israeli Spyware Firm That Accidentally Just Exposed Itself</a> - Massive OPSEC fail from the Paragon Solutions general counsel, who uploaded a photo of herself standing in front of a live spyware control panel that shows a target phone number from Czechia.</li>
<li><a href="https://www.theregister.com/2026/02/11/notepad_rce_flaw/" target="_blank">Notepad's new Markdown powers served with a side of remote code execution</a> - This one got a lot of hype but it does require a user to click a link inside a document. UNC paths also apparently work 🤦‍♂️.</li>
<li><a href="https://blog.ring.com/about-ring/ring-and-flock-cancel-partnership/" target="_blank">Ring and Flock Cancel Partnership</a> - "We determined the planned Flock Safety integration would require significantly more time and resources than anticipated." Or the backlash from the public actually worked to change course here?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.wietzebeukema.nl/blog/trust-me-im-a-shortcut" target="_blank">Trust Me, I’m a Shortcut</a> - LNKs are much more than simple links, they contain all kinds of information. When you stop following the specification and provide partial fields, or two fields of the same type Windows Explorer will often show different information than what the LNK will execute. Microsoft only considered one variant a CVE worthy, they all have security implications.</li>
<li><a href="https://embracethered.com/blog/posts/2026/scary-agent-skills/" target="_blank">Scary Agent Skills: Hidden Unicode Instructions in Skills ...And How To Catch Them</a> - AI agents/CLIs feel like the wild west. Hiding commands with <a href="https://embracethered.com/blog/ascii-smuggler.html" target="_blank">ASCII Smuggler</a> in SKILLS.md files can execute when the skill is used.</li>
<li><a href="https://bad-jubies.github.io/amduprof-1" target="_blank">AMD uProf Exploitation - Part One</a> The AMD driver <cite>AMDPowerProfiler.sys</cite> has a file write vulnerability that can be used for local privilege escalation.</li>
<li><a href="https://github.com/nettitude/ElephantPoint" target="_blank">ElephantPoint</a> is a C# module that will use SharePoint token to search and download files. Read more: <a href="https://www.lrqa.com/en/insights/articles/elephantpoint-a-sharepoint-enumeration-tool/" target="_blank">Introducing ElephantPoint</a>.</li>
<li><a href="https://clearbluejar.github.io/posts/how-llms-feed-your-re-habit-following-the-uaf-trail-in-clfs/" target="_blank">How LLMs Feed Your RE Habit: Following the Use-After-Free Trail in CLFS</a> - Some practical use of local LLMs (rare to see) reversing a use after free. If you can overlook the constant "this isn't X. It's Y" throughout the post it's got some good <a href="https://github.com/clearbluejar/pyghidra-mcp" target="_blank">pyghidra-mcp</a> use examples. One must assume the big exploit shops have automated RE churning on every update for target software.</li>
<li><a href="https://blog.lexfo.fr/munge-heap-buffer-overflow.html" target="_blank">Pwning Supercomputers - A 20yo vulnerability in Munge</a> - Going from <a href="https://aflplus.plus/" target="_blank">AFL++</a> fuzz to exploit in one of the authentication brokers commonly used in clustered high performance computer environments.</li>
<li><a href="https://blog.nviso.eu/2026/02/12/capture-the-kerberos-flag-detecting-kerberos-anomalies/" target="_blank">Capture the Kerberos Flag: Detecting Kerberos Anomalies</a> - Always good for red teams to check their tradecraft against what looks normal in an environment.</li>
<li><a href="https://eaton-works.com/2026/02/13/dava-india-hack/" target="_blank">Hacking a pharmacy to get free prescription drugs and more</a> - Blind POST requests eventually create a super admin account. Wild what is out there when you start looking closely and carefully crafting requests.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/wietze/lnk-it-up" target="_blank">lnk-it-up</a> - Project for generating and identifying deceptive LNK files.</li>
<li><a href="https://github.com/wunderwuzzi23/aid" target="_blank">aid</a> - A tool for detecting invisible Unicode characters in files, designed to identify potential ASCII smuggling attempts, hidden data encoding, and suspicious Unicode usage patterns.</li>
<li><a href="https://github.com/Bad-Jubies/Exploits/tree/main/AMD_uProf" target="_blank">AMD_uProf</a> - Exploit code for <a href="https://github.com/advisories/GHSA-r36r-8jrx-92cq" target="_blank">CVE-2025-61969</a>, incorrect permission assignment in AMD µProf may allow a local user-privileged attacker to achieve privilege escalation, potentially resulting in arbitrary code execution.</li>
<li><a href="https://github.com/dwisiswant0/sandboxec" target="_blank">sandboxec</a> - A lightweight command sandbox for Linux, secure-by-default, built on Landlock.</li>
<li><a href="https://github.com/Tzohar/PassLLM" target="_blank">PassLLM</a> - World's most accurate password guessing AI tool. A PyTorch implementation of PassLLM (USENIX 2025) that leverages PII and LoRA fine-tuning to outperform existing tools by over 45% on consumer hardware.</li>
<li><a href="https://github.com/Atsika/aznet" target="_blank">aznet</a> - The standard Go net.Conn interface using Azure Storage services as the transport layer.</li>
<li><a href="https://github.com/sliverarmory/reflektor" target="_blank">reflektor</a> is a Go library and CLI for loading shared libraries from bytes and invoking exported functions.</li>
<li><a href="https://github.com/MaorSabag/Adaptix-StealthPalace" target="_blank">Adaptix-StealthPalace</a> - Crystal Palace RDLL loader for Adaptix C2 with Ekko sleep obfuscation, IAT hooking via PICO, and per-section permission restoration.</li>
<li><a href="https://github.com/EricEsquivel/CobaltStrike-Linux-Beacon" target="_blank">CobaltStrike-Linux-Beacon</a> - Proof of Concept (PoC) implant for creating custom Cobalt Strike Beacons.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/hakwerk/labca" target="_blank">labca</a> - A private Certificate Authority for internal (lab) use, based on the open source ACME Automated Certificate Management Environment implementation from Let's Encrypt (tm).</li>
<li><a href="https://github.com/zer0condition/BusterCall" target="_blank">BusterCall</a> - "Bypassing" HVCI via donor PFN swaps to modify read-only code pages. Call chained kernel functions (kCET and SLAT support), modify read-only code pages, and more.</li>
<li><a href="https://github.com/Nova-Hunting/nova-proximity" target="_blank">nova-proximity</a> - Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA.</li>
<li><a href="https://github.com/preludeorg/cua-kit" target="_blank">cua-kit</a> - Tools for attacking Computer Use Agents.</li>
<li><a href="https://x.com/mattshumer_/status/2021256989876109403" target="_blank">[X] Something Big Is Happening</a> - Are we in the February 2020 before COVID stage of AI where a few vocal outcasts claiming massive change is coming while the world generally ignores them? With the last batch of models I am starting to believe the outcasts more and more.</li>
<li><a href="https://breachpool.com/" target="_blank">breachpool</a> - Predict the next ransomware target based on wisdom of the crowd.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+1)</p>
<p>Blogs monitored: 439 (+0)</p>
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
