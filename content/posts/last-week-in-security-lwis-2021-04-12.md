Title: Last Week in Security (LWiS) - 2021-04-12
Date: 2021-04-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-04-12
Author: Erik
Summary: 0-click Linux BT RCE (<a href="https://twitter.com/theflow0" target="_blank">@theflow0</a>), deanonymizing LinkedIn users (<a href="https://twitter.com/h3xstream" target="_blank">@h3xstream</a>), PPL demystified (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), HTML based remote macros (<a href="https://twitter.com/micahvandeusen" target="_blank">@micahvandeusen</a>), Chrome 0day-ish (<a href="https://twitter.com/r4j0x00" target="_blank">@r4j0x00</a>), wordlist generator (<a href="https://twitter.com/giteshnxtlvl" target="_blank">@giteshnxtlvl</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-04-05 to 2021-04-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.theguardian.com/world/2021/apr/11/israel-appears-confirm-cyberattack-iran-nuclear-facility" target="_blank">Israel appears to confirm it carried out cyberattack on Iran nuclear facility</a>. Stuxnet 2.0? Lots of hot takes on "infosec twitter." As I am not an expert in international relations, nuclear policy, diplomacy, or the role of cyber operations in any of the above I have no such hot takes.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2021/4/2/pwn2own-2021-schedule-and-live-results" target="_blank">Pwn2Own 2021 - Schedule and Live Results</a>. Lots of good exploits were shown at the latest Pwn2Own competition. Highlights: 0-Click Zoom RCE, Teams RCE, and five (!) Windows local privilege escalations.</li>
<li><a href="https://www.wired.com/story/signal-mobilecoin-payments-messaging-cryptocurrency/" target="_blank">Signal Adds a Payments Feature—With a Privacy-Focused Cryptocurrency</a>. I worry that this is scope creep on a grand scale. While signal still requires phone numbers for signup, they are busy implementing a venture capital backed and 100% pre-mined cryptocurrency (that Signal CEO Moxie is the CTO for)? Some have come to Signal's <a href="https://yorple.medium.com/in-defense-of-signal-45dd3395ba51" target="_blank">defense</a>, but I'm not convinced this is a good move. You either die a hero, or live long enough to see yourself become the villain.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://google.github.io/security-research/pocs/linux/bleedingtooth/writeup" target="_blank">BleedingTooth: Linux Bluetooth Zero-Click Remote Code Execution</a>. Yes, it's as crazy as it sounds. Be sure to check out the <a href="https://youtu.be/qPYrLRausSw" target="_blank">demo</a>. These kinds of exploits (zero-click network subsystem exploits) always amaze me.</li>
<li><a href="https://www.gosecure.net/blog/2021/04/07/deanonymizing-linkedin-users/" target="_blank">Deanonymizing LinkedIn Users</a>. This is a great OSINT article that shows how you can leverage LinkedIn to discover personal emails for individuals (useful in credential stuffing and phishing targeting). The API is limited to 1,000 requests every two days.</li>
<li><a href="https://itm4n.github.io/lsass-runasppl/" target="_blank">Do You Really Know About LSA Protection (RunAsPPL)?</a>. This article dives into the details of Protect Process Light, how it works, how it can be bypassed, and what the different PPL levels mean.</li>
<li><a href="https://micahvandeusen.com/html-maldoc-remote-macro-injection/" target="_blank">HTML Maldoc Remote Macro Injection</a>. Remote macros are useful to bypass mail scanning or other detection techniques that do not "detonate" the document. While it has been <a href="https://fortynorthsecurity.com/blog/maldoc-fu-some-ideas-for-malicious-document-delivery/" target="_blank">shown effective with .docx</a>, this is an interesting use case with HTML documents.</li>
<li><a href="https://labs.f-secure.com/blog/detecting-exposed-cobalt-strike-dns-redirectors" target="_blank">Detecting Exposed Cobalt Strike DNS Redirectors</a>. You are (hopefully) using HTTPS redirectors, but what about DNS redirectors to mask your C2 server's fingerprints? <a href="https://github.com/C-Sto/dnsfwd" target="_blank">dnsfwd</a> (LWiS 2021-03-22) would do nicely.</li>
<li><a href="https://github.com/commial/experiments/tree/master/windows-defender/ASR" target="_blank">Attack Surface Reduction</a> is a collection of research into Microsoft's Attack Surface Reduction rules. They are implemented in Lua, and the decompiled rules give lots of great information about easy things that instantly get marked "clean."</li>
<li><a href="https://www.wintellect.com/handling-open-file-security-warning/" target="_blank">Handling “Open File – Security Warning”</a>. The <cite>SEE_MASK_NOZONECHECKS</cite> environment variable is a new one to me, and it prevents the security pop up seen on downloaded files ("mark of the web"). While this won't help with your initial payload (that I can think of), it could be useful for follow on actions.</li>
<li><a href="https://github.com/NVISOsecurity/brown-bags/tree/main/DInvoke%20to%20defeat%20EDRs" target="_blank">DInvoke to defeat EDRs</a>. If aren't using Dinvoke with your C# you are missing out on all kinds of fun. This presentation walks through some of the existing research and packages it up nicely.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/0vercl0k/CVE-2021-24086" target="_blank">CVE-2021-24086</a> is a proof of concept for CVE-2021-24086 ("Windows TCP/IP Denial of Service Vulnerability "), a NULL dereference in tcpip.sys patched by Microsoft in February 2021. It is triggerable remotely by sending malicious UDP packet over IPv6. If you can reach an unpatched Windows machine with UDP over IPv6, you can bluescreen it. Put this one in the "demonstrate impact" folder and ensure your lawyer has reviewed whatever memo you got signed to allow its use on a customer.</li>
<li><a href="https://github.com/r4j0x00/exploits/commit/7ba55e5ab034d05877498e83f144e187d3ddb160" target="_blank">chrome "0day"</a>. It's really a 1day as the Chromium source has been patched but the patch hasn't been pushed to a release yet. It won't pop calc without the <cite>--no-sandbox</cite> flag, so bring your own sandbox escape!</li>
<li><a href="https://github.com/assetnote/kiterunner" target="_blank">kiterunner</a> is a "contextual content discovery tool" that uses traditional content discovery (throw a wordlist and look for non-error code responses), as well as more tailored requests with specific methods, headers, and parameters curated from multiple sources. More information at the <a href="https://blog.assetnote.io/2021/04/05/contextual-content-discovery/" target="_blank">assetnote blog</a>.</li>
<li><a href="https://github.com/xinbailu/TiEtwAgent" target="_blank">TiEtwAgent</a> is a PoC memory injection detection agent based on ETW, for offensive and defensive research purposes. Use this in your lab to see if your fancy tools can defeat kernel-mode detection!</li>
<li><a href="https://github.com/magnusstubman/dll-exports" target="_blank">dll-exports</a> is a collection of DLL function export forwards for DLL export function proxying. This is great for stealthy Windows persistence.</li>
<li><a href="https://github.com/giteshnxtlvl/cook" target="_blank">cook</a> is a customizable wordlist and password generator. It allows you to define word parts and patterns and generates all combinations - and the readme has beautiful usage pictures!</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
