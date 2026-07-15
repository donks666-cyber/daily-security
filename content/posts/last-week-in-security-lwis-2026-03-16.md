Title: Last Week in Security (LWiS) - 2026-03-16
Date: 2026-03-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-03-16
Author: Erik
Summary: Cascade 💉 (<a href="https://x.com/0xfluxsec" target="_blank">@0xfluxsec</a>), 🐍 for Conquest C2 (<a href="https://x.com/virtualloc" target="_blank">@virtualloc</a>), Outpacket (<a href="https://x.com/n00py1" target="_blank">@n00py1</a>), RegPwn (<a href="https://x.com/filip_dragovic" target="_blank">@filip_dragovic</a> + <a href="https://x.com/Flangvik" target="_blank">@Flangvik</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-03-02 to 2026-03-16.</p>
<aside class="m-block m-success">
<h3>Ludus 2!</h3>
<p>Our open source cyber range platform <a href="https://ludus.cloud" target="_blank">Ludus</a> reached version 2 last week! Check out the launch video <a href="https://www.youtube.com/watch?v=swa9k4QxeXA" target="_blank">here</a> and the <a href="https://docs.ludus.cloud/docs/upgrading-from-v1" target="_blank">upgrade docs</a>!</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.armadin.com/blog-posts/introducing-armadin" target="_blank">Introducing Armadin</a> - Kevin Mandia (of <cite>Mandiant</cite> fame) is back with a new company. This time he's gone to the dark side and is "building the ultimate attacker."</li>
<li><a href="https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/" target="_blank">Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker</a> - Sounds like Stryker's own device management software (Microsoft's InTune) was used to wipe the devices.</li>
<li><a href="https://engineering.fb.com/2026/03/02/data-infrastructure/investing-in-infrastructure-metas-renewed-commitment-to-jemalloc/" target="_blank">Investing in Infrastructure: Meta’s Renewed Commitment to jemalloc</a> - Meta un-archived the jemalloc project and, "are committed to continuing to develop jemalloc development with the open source community."</li>
<li><a href="https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz" target="_blank">It’s Official: Wiz Joins Google</a> - It took a year for Google to complete the acquisition of Wiz. Some lawyers must have made out well.</li>
<li><a href="https://www.engadget.com/social-media/meta-is-killing-end-to-end-encryption-in-instagram-dms-195207421.html" target="_blank">Meta is killing end-to-end encryption in Instagram DMs</a> - Meta has a negative incentive to support privacy. I'm shocked it was even an option to begin with.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2026/03/rip-regpwn/" target="_blank">RIP RegPwn</a> - "We kept it internal and used with great success across red team engagements since January 2025." The PoC video shows Windows running in VMware Workstation (I think). How much longer could this 0day have been kept alive if <a href="https://docs.ludus.cloud/docs/quick-start/testing-mode/" target="_blank">Ludus' testing mode</a> was used for discovery and testing/development, only exposing it on live operations vs the entire development cycle?</li>
<li><a href="https://www.atredis.com/blog/2026/3/12/findings-gadgets-like-its-2026" target="_blank">Finding Gadgets Like it’s 2026</a> - Java deserialization gadget chain finding via LLMs. Very 2026.</li>
<li><a href="https://offsec.almond.consulting/trust-no-one_are-one-way-trusts-really-one-way.html" target="_blank">Trust no one: are one-way trusts really one way?</a> - In order for "one way" trust to function, the truing domain must store the password of accounts created in the trusted domain. This allows a domain admin in the trusting domain to laterally move to the trusted domain. Not a new technique, but a new tool to accomplish it: <a href="https://github.com/AlmondOffSec/tdo_dump" target="_blank">tdo_dump</a></li>
<li><a href="https://fluxsec.red/implementing-early-cascade-injection-rust" target="_blank">Crimes against NTDLL - Implementing Early Cascade Injection</a> - These "hobby" C2 projects are getting pretty sophisticated.</li>
<li><a href="https://jakobfriedl.github.io/blog/conquest-modules/" target="_blank">Extending Conquest using Python Modules</a> - Speaking of advanced C2s, you can now extend Conquest with your own Python modules to create custom commands.</li>
<li><a href="https://labs.infoguard.ch/posts/decrypting-and-abusing_paloalto-cortex-xdr_behavioral-rules_biocs/" target="_blank">Decrypting and Abusing Predefined BIOCs in Palo Alto Cortex XDR</a> - Knowing the rules that will trigger an alert in your target's EDR is a huge advantage. The "global whitelist" was a juicy find. Looks like the plain text rules repo is 404ing now though...</li>
<li><a href="https://blog.quarkslab.com/pagejack-in-action-cve-2022-0995-exploit.html" target="_blank">PageJack in Action: CVE-2022-0995 exploit</a> - A new technique (<a href="https://phrack.org/issues/71/13#article" target="_blank">PageJack</a>) for an "old" exploit (CVE-2022-0995) and a cool write up with a PoC!</li>
<li><a href="https://specterops.io/blog/2026/03/10/the-nemesis-2-x-development-guide/" target="_blank">The Nemesis 2.X Development Guide</a> - Nemesis is a "one stop shop" backend for red team data collection and "enrichment" and the 2.X release makes it easier to add your own modules (file types, C2 connections, etc.).</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://lists.gnu.org/archive/html/bug-inetutils/2026-03/msg00031.html" target="_blank">Remote Pre-Auth Buffer Overflow in GNU Inetutils telnetd (LINEMODE SLC)</a> - Looks like someone is taking an interest in telnetd... Needs an ASLR bypass on modern systems, but who is running <cite>telnetd</cite> on modern systems. Embedded devices are a great target for this sort of thing.</li>
<li><a href="https://github.com/mdsecactivebreach/RegPwn" target="_blank">RegPwn</a> Exploit code for LPE in Windows clients and servers (CVE-2026-24291).</li>
<li><a href="https://github.com/Flangvik/RegPwnBOF" target="_blank">RegPwnBOF</a> - Cobalt Strike BOF port of the RegPwn exploit by Filip Dragovic (@Wh04m1001) / MDSec ActiveBreach.</li>
<li><a href="https://github.com/atredispartners/llmchainhunter" target="_blank">llmchainhunter</a> - This repo contains the design plan and runbook for using Claude Code to search for Java Deserialization Gadget chains.</li>
<li><a href="https://github.com/matteyeux/coruna" target="_blank">coruna</a> - The actual exploits and binaries from last week's Coruna iOS exploit kit.</li>
<li><a href="https://github.com/zux0x3a/Phantom" target="_blank">Phantom</a> - Phantom is project created to perform loading and executing .NET assemblies directly in memory within an IIS environment running in full‑trust mode. Instead of relying on file‑based approach, it uses reflective loading techniques to inject and run a DLL inside the memory space of the w3wp.exe worker pool process</li>
<li><a href="https://github.com/klezVirus/BYOUD" target="_blank">BYOUD</a> is a framework for x64 stack spoofing on Windows. It tackles a complete opposite approach from classic stack spoofing, manipulating unwind metadata to hide arbitrary chunks of the call chain in debuggers and EDRs.</li>
<li><a href="https://github.com/memN0ps/doublepulsar-rs" target="_blank">doublepulsar-rs</a> - Rusty DoublePulsar - Cobalt Strike User-Defined Reflective Loader (UDRL) in Rust (Codename: DoublePulsar)</li>
<li><a href="https://github.com/memN0ps/armory-rs" target="_blank">armory-rs</a> - Rust Beacon Object Files (BOFs) for adversary simulation, threat emulation, security research, and detection engineering. All 115 TrustedSec BOFs ported from C to Rust using the rustbof framework.</li>
<li><a href="https://github.com/AeonDave/AdaptixC2-Template-Generators" target="_blank">AdaptixC2-Template-Generators</a> - Standalone scaffolding toolkit for AdaptixC2 extender development. Generates ready-to-implement stub projects for agents, listeners, services (optionally with post-build wrapper pipeline), and custom wire protocols -- all compatible with the axc2 v1.2.0 plugin API.</li>
<li><a href="https://github.com/svnscha/mcp-windbg" target="_blank">mcp-windbg</a> - A Model Context Protocol server that bridges AI models with WinDbg for crash dump analysis and remote debugging.</li>
<li><a href="https://github.com/n00py/Outpacket" target="_blank">Outpacket</a> - Tired of impacket? This cheatsheet maps common impacket workflows to their modern alternatives</li>
<li><a href="https://github.com/0xROOTPLS/Fritter" target="_blank">Fritter</a> is a heavily modified fork of TheWover and Odzhan's Donut shellcode generator. It generates position-independent shellcode for in-memory execution of VBScript, JScript, EXE, DLL, and .NET assemblies, but with a heavy focus on evasion and signature resistance.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=MhJoJRqJ0Wc" target="_blank">$75,000,000 Crypto Wallet Bulk Hack</a> - Ultimate proof that physical access == root access. No matter how many secure enclaves or hardware security modules you have, if the attacker is dedicated enough and has physical access, with enough time and resources they can get in.</li>
<li><a href="https://github.com/eonsystemspbc/fly-brain" target="_blank">fly-brain</a> - Whole-brain leaky integrate-and-fire model of the adult fruit fly, built from the FlyWire connectome (~138k neurons, ~5M synapses). 🤯</li>
<li><a href="https://github.com/Beingpax/VoiceInk" target="_blank">VoiceInk</a> - Voice-to-text app for macOS to transcribe what you say to text almost instantly</li>
<li><a href="https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket" target="_blank">MANPADS-System-Launcher-and-Rocket</a> - 👀</li>
<li><a href="https://github.com/NawfalMotii79/PLFM_RADAR" target="_blank">PLFM_RADAR</a> - Open-source, low-cost 10.5 GHz PLFM phased array RADAR system</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 442 (+0)</p>
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
