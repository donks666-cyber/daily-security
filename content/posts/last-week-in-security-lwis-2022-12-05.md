Title: Last Week in Security (LWiS) - 2022-12-05
Date: 2022-12-05 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-12-05
Author: Erik
Summary: ChatGPT (<a href="https://twitter.com/OpenAI" target="_blank">@OpenAI</a>), Huawei hypervisor research (<a href="https://twitter.com/lyte__" target="_blank">@lyte__</a> + <a href="https://twitter.com/NeatMonster_" target="_blank">@NeatMonster_</a>), Tailscale DNS rebiding attacks (<a href="https://twitter.com/JJJollyjim" target="_blank">@JJJollyjim</a>), Using CodeQL to find RCE (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), PPLcontrol (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-11-28 to 2022-12-05.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://openai.com/blog/chatgpt/" target="_blank">ChatGPT: Optimizing Language Models for Dialogue</a>. Well, this exploded last week. If you haven't tried it, it's worth some specific technical queries. You can even <a href="https://thezvi.substack.com/p/jailbreaking-the-chatgpt-on-release" target="_blank">jailbreak it</a> or run a <a href="https://www.engraved.blog/building-a-virtual-machine-inside/" target="_blank">'virtual machine'</a> in it.</li>
<li><a href="https://www.macrumors.com/2022/11/29/eufy-camera-cloud-uploads-no-user-consent/" target="_blank">Anker's Eufy Cameras Caught Uploading Content to the Cloud Without User Consent</a>. While it was only thumbnail images being uploaded, still a bad look for a brand that is heavy on "local only" branding. Compared to Ring cameras that will <a href="https://support.ring.com/hc/en-us/articles/360032492292-Amazon-Sidewalk-Information" target="_blank">find their own wifi</a> to steam video to the cloud, this seems minor. Put your cameras on a VLAN without egress, and VPN in to view them - trust no one.</li>
<li><a href="https://www.washingtonpost.com/technology/2022/11/30/trustcor-internet-authority-mozilla/" target="_blank">Web browsers drop mysterious company with ties to U.S. military contractor</a>. Props to The Washington Post for exposing the root CA and finally getting enough pressure to have it removed from browsers (12 years too late?).</li>
<li><a href="https://www.freebsd.org/security/advisories/FreeBSD-SA-22:15.ping.asc" target="_blank">The FreeBSD Project - Stack overflow in ping(8)</a>. Despite the scary title, it only applies to ping responses, and the ping process "runs in a capability mode sandbox on all affected versions of FreeBSD and is thus very constrained in how it can interact with the rest of the system at the point where the bug can occur." I doubt this will yield remote shells any time soon. LPE however...</li>
<li><a href="https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html" target="_blank">Memory Safe Languages in Android 13</a>. No memory safety related bugs in the Rust code added to Android (yet). It's not a magic bullet, but the evidence shows it really does help prevent memory safety bugs.</li>
<li><a href="https://twitter.com/samwcyo/status/1597695281881296897" target="_blank">We recently found a vulnerability affecting Hyundai and Genesis vehicles where we could remotely control the locks, engine, horn, headlights, and trunk of vehicles made after 2012</a>. Control character injection lets you register emails that "matched" actual users, and thereby take over their car via the internet. What a time to be alive. Not broad enough? What about <a href="https://twitter.com/samwcyo/status/1597792097175674880" target="_blank">taking over multiple brands of cars via SiriusXM?</a>.</li>
<li><a href="https://www.wiz.io/blog/hells-keychain-supply-chain-attack-in-ibm-cloud-databases-for-postgresql" target="_blank">Hell's Keychain: Supply-chain vulnerability in IBM Cloud Databases for PostgreSQL allows potential unauthorized database access</a>. Potential access to the CI of the IBM cloud. Yikes!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.impalabs.com/2212_huawei-security-hypervisor.html" target="_blank">Shedding Light on Huawei's Security Hypervisor</a>. This post tears apart the encrypted security hypervisor used in Huawei devices and nets a CVE: <a href="https://blog.impalabs.com/2212_advisory_huawei-security-hypervisor.html" target="_blank">CVE-2021-39979 OOB Accesses Using the Logging System</a>.</li>
<li><a href="https://emily.id.au/tailscale" target="_blank">CVE-2022-41924 - RCE in Tailscale, DNS Rebinding, and You</a>. The rebinding attacks are neat (if a bit hard to pull off in the real world), but the vendor response is downright amazing, and in a good way this time!</li>
<li><a href="https://frycos.github.io/vulns4free/2022/12/02/rce-in-20-minutes.html" target="_blank">Pre-Auth RCE with CodeQL in Under 20 Minutes</a>. CodeQL is a force multiplier, I've said it before and I'll say it again.</li>
<li><a href="https://itm4n.github.io/debugging-protected-processes/" target="_blank">Debugging Protected Processes</a>. Debugging protected processes on Windows can be tricky, so what if you made your debugger have the same level of protection instead? Now you can with <a href="https://github.com/itm4n/PPLcontrol" target="_blank">PPLcontrol</a>.</li>
<li><a href="https://posts.specterops.io/stalking-inside-of-your-chromium-browser-757848b67949" target="_blank">Stalking inside of your Chromium Browser</a>. Browsers are where lots of important information is accessed. If you don't have good access methods to leverage endpoint access to dump browser information, or better yet live inside the browser, you should prioritize development.</li>
<li><a href="https://medium.com/tenable-techblog/how-to-mimic-kerberos-protocol-transition-using-reflective-rbcd-a4984bb7c4cb" target="_blank">How to mimic Kerberos protocol transition using reflective RBCD</a>. Kerberos contains more foot-guns than any authentication protocol I've seen.</li>
<li><a href="https://mjg59.dreamwidth.org/62175.html" target="_blank">Making unphishable 2FA phishable</a>. Thanks to non-input enabled devices, even the best 2FA can be phished (sometimes).</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Wh04m1001/SysmonEoP" target="_blank">SysmonEoP</a> - Proof of Concept for arbitrary file delete/write in Sysmon (CVE-2022-41120).</li>
<li><a href="https://github.com/google/security-research/security/advisories/GHSA-pw56-c55x-cm9m" target="_blank">Visual Studio Code: Remote Code Execution</a>. Jypiter notebook links could have led to RCE in vscode when clicked.</li>
<li><a href="https://github.com/klezVirus/SilentMoonwalk" target="_blank">SilentMoonwalk</a> is a PoC implementation of a true call stack spoofer, implementing a technique to remove the original caller from the call stack, using ROP to desynchronize unwinding from control flow. Want it in rust? Try <a href="https://github.com/Kudaes/Unwinder" target="_blank">Unwinder</a>.</li>
<li><a href="https://github.com/BeichenDream/PrintNotifyPotato" target="_blank">PrintNotifyPotato</a> - Another potato, using PrintNotify COM service for lifting rights.</li>
<li><a href="https://github.com/knight0x07/BumbleCrypt" target="_blank">BumbleCrypt</a> - A Bumblebee-inspired Crypter.</li>
<li><a href="https://gist.github.com/ustayready/3ba2e4b1a4ec3cdad188f0f7d0dc4b73" target="_blank">google_lure.py</a> -  Generate phishing lures that exploit open-redirects from www.google.com using Google Docs.</li>
<li><a href="https://github.com/byt3bl33d3r/NimDllSideload" target="_blank">NimDllSideload</a> allows you to easily generate Nim DLLs you can use sideloading/proxy loading. If you're unfamiliar with what DLL sideloading is, take a gander at this <a href="https://redteaming.co.uk/2020/07/12/dll-proxy-loading-your-favorite-c-implant/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/EspressoCake/Defender_Exclusions-BOF" target="_blank">Defender_Exclusions-BOF</a> - A BOF to determine Windows Defender exclusions.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Aetsu/Neton" target="_blank">Neton</a> is a tool for getting information from Internet connected sandboxes.</li>
<li><a href="https://github.com/kubeshark/kubeshark" target="_blank">kubeshark</a> , the API Traffic Viewer for kubernetes, provides deep visibility and monitoring of all API traffic and payloads going in, out and across containers and pods inside a Kubernetes cluster. Think of a combination of Chrome Dev Tools, TCPDump and Wireshark, re-invented for Kubernetes.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 329 (+1)</p>
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
