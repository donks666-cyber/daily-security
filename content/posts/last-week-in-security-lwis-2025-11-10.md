Title: Last Week in Security (LWiS) - 2025-11-10
Date: 2025-11-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-11-10
Author: Erik
Summary: Apple's sourcemaps takedown (<a href="https://x.com/moeruri" target="_blank">@moeruri</a>), Call stack sig bypass (<a href="https://x.com/SAERXCIT" target="_blank">@saerxcit</a>), AD Site pwnage (<a href="https://x.com/croco_byte" target="_blank">@croco_byte</a>), sneaky remap (<a href="https://x.com/magisterquis" target="_blank">@MagisterQuis</a>), Deceptiq launch (<a href="https://x.com/deceptiq_" target="_blank">@deceptiq_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-11-03 to 2025-11-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://github.com/github/dmca/blob/master/2025/11/2025-11-05-apple.md" target="_blank">Apple's DCMA takedown request for apps.apple.com sourcemaps</a> - When the web version of the Apple app store was launched recently, it included javascript "sourcemaps" that made it easy to recreate the original javascript source code of the frontend. This is commonly used in development, but usually stripped from a production build when the source code is minified. While not a security issue, the sourcemaps did include references to internal issues, TODO comments, and the like. <a href="https://codeberg.org/JoanVC/apps.apple.com" target="_blank">The internet never forgets</a>.</li>
<li><a href="https://openai.com/index/introducing-aardvark/" target="_blank">Introducing Aardvark: OpenAI’s agentic security researcher</a> - Begun, the big AI lab's security researcher wars have. Google's entrant: <a href="https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/" target="_blank">Introducing CodeMender: an AI agent for code security</a>.</li>
<li><a href="https://discuss.linuxcontainers.org/t/announcing-incusos/25139/1" target="_blank">Announcing IncusOS</a> - I've been keeping a close eye on <a href="https://linuxcontainers.org/incus/" target="_blank">Incus</a> (the community fork of the LXC container manager), and a dedicated OS is a cool addition to the ecosystem.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://offsec.almond.consulting/evading-elastic-callstack-signatures.html" target="_blank">Evading Elastic EDR's call stack signatures with call gadgets</a> - Use a benign DLL with a call gadget to break up the suspect call stack which breaks Elastic EDR's detection. Easy to test this in <a href="https://ludus.cloud" target="_blank">Ludus</a> with the <a href="https://docs.ludus.cloud/docs/environment-guides/elastic" target="_blank">Elastic Security Lab</a>.  Code at <a href="https://github.com/AlmondOffSec/LibTPLoadLib" target="_blank">LibTPLoadLib</a>.</li>
<li><a href="https://aff-wg.org/2025/11/10/tradecraft-engineering-with-aspect-oriented-programming/" target="_blank">Tradecraft Engineering with Aspect-Oriented Programming</a> - Mudge introduces a new feature to Crystal Palace, hooking! You can now chain hooks that modify how an API call is executed.</li>
<li><a href="https://www.synacktiv.com/en/publications/site-unseen-enumerating-and-attacking-active-directory-sites" target="_blank">Site Unseen: Enumerating and Attacking Active Directory Sites</a> - Quentin Roland shows the power of Sites in Active Directory and contributed <a href="https://github.com/SpecterOps/SharpHound/pull/186" target="_blank">pull requests</a> to SharpHound/Bloohound. Sites, like other Active Directory objects,</li>
<li><a href="https://labs.watchtowr.com/whats-that-coming-over-the-hill-monsta-ftp-remote-code-execution-cve-2025-34299/" target="_blank">What’s That Coming Over The Hill? (Monsta FTP Remote Code Execution CVE-2025-34299)</a> - "Managed File Transfer" applications are notoriously vulnerable pieces of "enterprise" tech.</li>
<li><a href="https://blog.pixelmelt.dev/kindle-web-drm/" target="_blank">How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked</a> - I can't help but think how much human time was wasted on both ends of this, the obfuscation and the reverse engineering. Simson Garfinkel (creator of <a href="https://github.com/simsong/bulk_extractor" target="_blank">bulk_extractor</a>) once told me he doesn't do "file cabinet forensics," that is, forensic analysis/reverse engineering where the solution is in a file cabinet somewhere, just unavailable to the public (i.e. proprietary). The lengths Amazon has gone to obfuscate ebooks are just lots more files in the file cabinet.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MorDavid/donpwner" target="_blank">DonPwner</a> - Advanced Domain Controller attack and credential analysis tool leveraging DonPAPI database.</li>
<li><a href="https://github.com/r3drun3/magnet" target="_blank">magnet</a> - Purple-team telemetry &amp; simulation toolkit.</li>
<li><a href="https://github.com/magisterquis/srsocwamof" target="_blank">srsocwamof</a> - Sneaky Remap - Shared Object Cloaking with a Minimum of Fuss ~ BSides Berlin 2025.</li>
<li><a href="https://github.com/EvilBytecode/ExitPatcher" target="_blank">ExitPatcher</a> - Prevent in-process process termination by patching exit APIs.</li>
<li><a href="https://github.com/winsecurity/MaleficentVM" target="_blank">MaleficentVM</a> - This is practice VM for malware development.</li>
<li><a href="https://github.com/diversenok/DiaSymbolView" target="_blank">DiaSymbolView</a> - PDB file inspection tool.</li>
<li><a href="https://github.com/BlWasp/PhantomTask" target="_blank">PhantomTask</a> - A tool to play with scheduled tasks on Windows, in Rust.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://dfir.ch/posts/today_i_learned_binfmt_misc/" target="_blank">Today I learned: binfmt_misc</a> - Register a SUID binary as a custom format for a nice Linux backdoor.</li>
<li><a href="https://github.com/SECFORCE/LLMGoat" target="_blank">LLMGoat</a> - This project is a deliberately vulnerable environment to learn about LLM-specific risks based on the OWASP Top 10 for LLM Applications.</li>
<li><a href="https://deceptiq.com/" target="_blank">Operationalize Adversary Behaviors Into Actionable Alerts</a> - Deceptiq launched its canary token service. No affiliation, just a fan of canary tokens and Rad (see: <a href="https://www.youtube.com/watch?v=TfG9lBYCOq8" target="_blank">Writing Tiny, Efficient, And Reliable Malware by Rad Kawar</a>).</li>
<li><a href="https://github.com/wesmar/kvc" target="_blank">kvc</a> - KVC enables unsigned driver loading via DSE bypass (g_CiOptions patch/skci.dll hijack) and PP/PPL manipulation for LSASS memory dumping on modern Windows with HVCI/VBS.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 490 (+1)</p>
<p>Blogs monitored: 435 (+1)</p>
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
