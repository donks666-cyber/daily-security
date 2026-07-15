Title: Last Week in Security (LWiS) - 2025-12-08
Date: 2025-12-08 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-12-08
Author: Erik
Summary: SCOM lab (<a href="https://x.com/synzack21" target="_blank">@synzack21</a>), WatchGuard RCE (<a href="https://x.com/_McCaulay" target="_blank">@_mccaulay</a>), Clickjacking with SVGs (<a href="https://x.com/rebane2001" target="_blank">@rebane2001</a>), macOS LPE (<a href="https://x.com/theevilbit" target="_blank">@theevilbit</a>), a new private phone company (<a href="https://x.com/nickcalyx" target="_blank">@nickcalyx</a> + <a href="https://x.com/phreeli" target="_blank">@phreeli</a>), Proxmox tradecraft (<a href="https://x.com/ZephrFish" target="_blank">@ZephrFish</a>) and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-12-02 to 2025-12-08.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.mooreslawisdead.com/post/sam-altman-s-dirty-dram-deal" target="_blank">Sam Altman’s Dirty DRAM Deal</a> - We've seen RAM prices absolutely explode in the past two months, and this is why. There are only three manufacturers of DRAM (Samsung, Micron, and SK Hynix), and with two of them making a deal with OpenAI, Micron got slammed by everyone else to get orders so hard it's going to completely <a href="https://finance.yahoo.com/news/micron-exits-crucial-consumer-memory-053140808.html" target="_blank">exit the consumer memory business</a> and only sell to enterprise customers. Bad time to be a consumer. We're moving to a world of centralized computing and thin clients. I'm still rooting for someone to <a href="https://tinygrad.org/#faq" target="_blank">commoditize the petaflop</a>.</li>
<li><a href="https://security.googleblog.com/2025/12/architecting-security-for-agentic.html" target="_blank">Architecting Security for Agentic Capabilities in Chrome</a> - The solution for securing "agentic capabilities" (preventing AI mistakes) is to check the first AI with a second AI? It's <a href="https://en.wikipedia.org/wiki/Turtles_all_the_way_down" target="_blank">turtles all the way down</a>!</li>
<li><a href="https://www.wired.com/story/new-anonymous-phone-carrier-sign-up-with-nothing-but-a-zip-code/" target="_blank">A New Anonymous Phone Carrier Lets You Sign Up With Nothing but a Zip Code</a> - "Nothing but a Zip Code" happens to be a "Zip+4" code, a more precise version that usually narrows down the address to &lt; 20 people. How many of your neighbors are signing up for this new phone service? <a href="https://www.phreeli.com/" target="_blank">Phreeli</a> is the service. The ability to use eSIMs (no physical SIM card) means that Phreeli never has to know your real shipping address and you can pay with Monero, but remember that your phone still has an unique ID (<a href="https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity" target="_blank">IMEI</a>) and has to connect to the T-Mobile cell towers.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.offsec.com/blog/cve-2025-55182/?utm_campaign=9872414-2025-Technical-Blog&amp;utm_content=360856436&amp;utm_medium=social&amp;utm_source=twitter&amp;hss_channel=tw-134994790" target="_blank">CVE-2025-55182 – React Server Components RCE via Flight Payload Deserialization</a> - This feels similar to <a href="https://en.wikipedia.org/wiki/Shellshock_(software_bug)" target="_blank">Shellshock</a> (the Bash bug you could trigger on CGI sites via headers), but for React (and uses deserialization instead of function export trickery). Vulncheck has a few <a href="https://www.vulncheck.com/blog/react2shell-canaries" target="_blank">samples</a>.</li>
<li><a href="https://labs.watchtowr.com/yikes-watchguard-fireware-os-ikev2-out-of-bounds-write-cve-2025-9242/" target="_blank">yIKEs (WatchGuard Fireware OS IKEv2 Out-of-Bounds Write CVE-2025-9242)</a> - McCaulay Hudson lands their first blog post for watchTowr and has gotten the memo on the watchTowr format: snark, memes, and solid technical writeups. These security appliance vulnerabilities always remind me of the <a href="https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Ffjx476edxnhc1.jpeg" target="_blank">chain of firewalls</a> meme.</li>
<li><a href="https://bishopfox.com/blog/arista-nextgen-firewall-xss-to-rce-chain" target="_blank">Arista NextGen Firewall XSS to RCE Chain</a> - Antother security applicance vulnerability, but this one requires an admin to click a malicious link while logged in to get remote code execution, so less egregious. Still want more enterprise security appliance vulnerabilities? Jon Williams also dropped: <a href="https://bishopfox.com/blog/fortinet-fortiweb-authentication-bypass-cve-2025-64446" target="_blank">Fortinet FortiWeb Authentication Bypass</a>.</li>
<li><a href="https://lyra.horse/blog/2025/12/svg-clickjacking/" target="_blank">SVG Filters - Clickjacking 2.0</a> - Clickjacking as a technique is not talked about much any more (thanks to browser security features like X-Frame-Options, and Content Security Policy), but perhaps the nearly turing-complete nature of SVGs will bring it back!</li>
<li><a href="https://theevilbit.github.io/posts/localized/" target="_blank">macOS LPE via the .localized directory</a> - This would be tricky to use operationally. You'd need to be able to write to <cite>/Applications</cite> and then convince the user to install a vulnerable application. Not impossible, but not immediately operationally viable. Perhaps bundling a vulnerable application in a handler that pre-creates the "exploit" app would work to get initial access + privilege escalation?</li>
<li><a href="https://www.fortinet.com/blog/threat-research/uncovering-hidden-forensic-evidence-in-windows-mystery-of-autologger" target="_blank">Uncovering Hidden Forensic Evidence in Windows: The Mystery of AutoLogger-Diagtrack-Listener.etl</a> - Microsoft's "Customer Experience Improvement Program (CEIP)" may store useful logs for incident responders, but how it functions, or is even enabled remains opaque.</li>
<li><a href="https://tishina.in/ops/sambadc" target="_blank">sambadc</a> - I have never seen a Samba based directory controller in a production environment, but I'm sure they exist. If you need to attack them, there are some gotchas detailed here.</li>
<li><a href="https://blog.zsec.uk/lolprox/" target="_blank">Living off the Hypervisor - LOLPROX</a> - Some good Proxmox tradecraft. If you look at the VM names in Andy's examples you'll recognize them as <a href="https://ludus.cloud" target="_blank">Ludus</a> VMs 😊. Comes with a version for <a href="https://blog.zsec.uk/lolprox-defend/" target="_blank">Defenders</a> as well.</li>
<li><a href="https://specterops.io/blog/2025/12/09/git-scommit-putting-the-ops-in-opsmgr/" target="_blank">Git SCOMmit – Putting the Ops in OpsMgr</a> - "As a red team operator, while I may not always be conducting the research, I need an environment where I can reliably test all the new tradecraft my team puts out and know how to perform these attacks in real environments. Historically, if you have ever set up something like SCCM, you know how painful some of the installs are, and how many different variables you can introduce during setup that may or may not be representative of real-world installs. Or after so many exploits, you find your lab in a broken state and maybe your snapshot hygiene hasn’t been great lately. These were the exact types of problems I love solving with automation, and my tool of choice for doing this is ansible scripts deployed with my <a href="https://ludus.cloud" target="_blank">Ludus</a> environment in my home lab." Exactly the use case for <a href="https://ludus.cloud" target="_blank">Ludus</a>!</li>
<li><a href="https://www.outflank.nl/blog/2025/12/09/seccomp-notify-injection/" target="_blank">Linux Process Injection via Seccomp Notifier</a> - A novel Linux process injection technique with a few limitations, the biggest being that you can only inject into child processes.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_12.0_build/Ghidra/Configurations/Public_Release/src/global/docs/WhatsNew.md#whats-new-in-ghidra-120" target="_blank">Ghidra 12.0</a> - Your favorite NSA open source decompiler got a major version bump.</li>
<li><a href="https://oswatcher.github.io/frontend/" target="_blank">OS Watcher v0.3</a> - Explore Windows evolution from Win95 ➡️ Win11-24H2 (with updates !) and a Registry explorer. File download is disabled, for obvious reasons.</li>
<li><a href="https://github.com/pard0p/LibPicoManager" target="_blank">LibPicoManager</a> - LibPicoManager is a unified PICO management framework that provides centralized control over PICOs in memory, enabling dynamic code loading, runtime PICO substitution, and advanced evasion techniques like sleep masking through a single RWX code block.</li>
<li><a href="https://github.com/dabit3/fabricate" target="_blank">fabricate</a> - An experimental research tool for fabricating GitHub personas with AI-generated repositories.</li>
<li><a href="https://github.com/Xenov-X/csbot" target="_blank">csbot</a> - Golang Automation Framework for Cobalt Strike using the Rest API.</li>
<li><a href="https://github.com/Synzack/ludus_scom" target="_blank">ludus_scom</a> - An Ansible collection that installs a SCOM deployment with optional configurations.</li>
<li><a href="https://github.com/outflanknl/seccomp-notify-injection" target="_blank">seccomp-notify-injection</a> - Linux Process Injection via Seccomp Notifier.</li>
<li><a href="https://github.com/dis0rder0x00/stillepost" target="_blank">stillepost</a> - Using Chromium-based browsers as a proxy for C2 traffic.</li>
<li><a href="https://github.com/martinsohn/ADAttributeHound" target="_blank">ADAttributeHound</a> - ADAttributeHound is an OpenGraph extension for BloodHound that exports Active Directory custom attributes as node properties.</li>
<li><a href="https://github.com/donlon/cloudflare-error-page" target="_blank">cloudflare-error-page</a> - Cloudflare error page generator. [Great for phishing page decoys]</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/zero2504/Fairy-Law" target="_blank">Fairy-Law</a> - Compromise or disable EDR security solutions.</li>
<li><a href="https://workspaceupdates.googleblog.com/2025/04/emoji-reactions-in-gmail.html" target="_blank">Express yourself and quickly respond to emails with emojis reactions in Gmail</a> - This feels like a feature that can somehow be abused for information gathering, phishing, or the like. If anyone digs into it, please publish your findings and let us know!</li>
<li><a href="https://github.com/Linux-Platform-Kit" target="_blank">Linux Platform Kit</a> - An open source Linux handheld (in development).</li>
<li><a href="https://amber-lang.com/" target="_blank">Amber: A language compiled to Bash.</a> - I've always said if your bash script is over 50 lines it should be written in a better language.</li>
<li><a href="https://github.com/ziggy42/epsilon" target="_blank">epsilon</a> - A WASM virtual machine written in Go with 0 dependencies.</li>
<li><a href="https://github.com/P0142/LDAP-Bof-Collection" target="_blank">LDAP-Bof-Collection</a> - Collection of many ldap bofs for domain enumeration and privilege escalation. Created for use with the Adaptix C2.</li>
<li><a href="https://www.youtube.com/watch?v=iu5rnQkfO6M" target="_blank">Coding Trance Music from Scratch (Again )</a> - "In the beginning there were five notes."</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 490 (+0)</p>
<p>Blogs monitored: 436 (+0)</p>
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
