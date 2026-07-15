Title: Last Week in Security (LWiS) - 2021-08-16
Date: 2021-08-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-08-16
Author: Erik
Summary: ProFTPd UAF (<a href="https://twitter.com/lockedbyte" target="_blank">@lockedbyte</a>), API hacking (<a href="https://twitter.com/hakluke" target="_blank">@hakluke</a> and <a href="https://twitter.com/farah_hawaa" target="_blank">@Farah_Hawaa</a>), file ext tricks (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), built-in AD searching w/ADSI (<a href="https://twitter.com/Gr1mmie" target="_blank">@Gr1mmie</a>), DCE/RPC fingerprints (<a href="https://twitter.com/hdmoore" target="_blank">@hdmoore</a>), SAML issues (<a href="https://twitter.com/joonas_fi" target="_blank">@joonas_fi</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-08-09 to 2021-08-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.washingtonpost.com/technology/2021/08/10/apple-drops-corellium-lawsuit/" target="_blank">Apple drops intellectual property lawsuit against maker of security tools</a>. The battle against the virtual iOS device host finally ends with a fizzle. The case was scheduled to start next week. "The terms of the settlement were confidential."</li>
<li><a href="https://www.wired.com/story/ai-phishing-emails/" target="_blank">AI Wrote Better Phishing Emails Than Humans in a Recent Test</a>. This is the dystopian future we were promised.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://adepts.of0x.cc/proftpd-cve-2020-9273-exploit/" target="_blank">Having fun with a Use-After-Free in ProFTPd (CVE-2020-9273)</a>. This post analyzes the ProFTPd vulnerability and how to exploit it bypassing all the memory exploit mitigations present by default (ASLR, PIE, NX, Full RELRO, Stack Canaries etc). Two different exploits available at <a href="https://github.com/lockedbyte/CVE-Exploits/tree/master/CVE-2020-9273" target="_blank">CVE-2020-9273</a>.</li>
<li><a href="https://labs.detectify.com/2021/08/10/how-to-hack-apis-in-2021/" target="_blank">How to Hack APIs in 2021</a>. Type confusion, JWTs, undocumented APIs, versioning, rate limiting, race conditions, XXE injection, switching content types, HTTP methods, injection vulnerabilities, and more are covered in this great post.</li>
<li><a href="https://research.securitum.com/comparison-of-reverse-image-searching-in-popular-search-engines-osint-hints/" target="_blank">Comparison of reverse image searching in popular search engines [OSINT hints]</a>. TLDR: consider Yandex next time you need to reverse search an image.</li>
<li><a href="https://blog.cobaltstrike.com/2021/08/11/teamserver-prop/" target="_blank">TeamServer.prop</a>. Have you been wondering what those TeamServer.prop warnings were in Cobalt Strike 4.4? It turns out you can tweak the screenshot and keylog callback data settings to customize how the team server handles <a href="https://labs.sentinelone.com/hotcobalt-new-cobalt-strike-dos-vulnerability-that-lets-you-halt-operations/" target="_blank">potentially DoS-able</a> data.</li>
<li><a href="https://blog.thecybersecuritytutor.com/spoofing-file-extensions-using-gdrive-and-onedrive/" target="_blank">Spoofing File Extensions Using Google Drive and OneDrive</a>. The tricks in this post may be helpful when/if you deliver payloads via email.</li>
<li><a href="https://posts.specterops.io/thoughts-on-detection-3c5cab66f511" target="_blank">Playing Detection with a Full Deck</a>. If you've ever done any Purple teaming, this post will hit home. Understanding the full context of a system (i.e. how are services created) is critical to good detection rules.</li>
<li><a href="https://pwnshift.github.io/2021/08/12/hashes.html" target="_blank">Phishing for NetNTLM Hashes</a>. There are many ways to leak NTLM hashes but this post shows the results of testing and Security Zones are treated by web clients. Once you have NTLM and network access, this <a href="https://www.thehacker.recipes/ad-ds/movement/ntlm/relay" target="_blank">relay</a> page has amazing charts for what is possible.</li>
<li><a href="https://www.secureworks.com/blog/going-for-the-gold-penetration-testing-tools-exploit-golden-saml" target="_blank">Going for the Gold: Penetration Testing Tools Exploit Golden SAML</a>. Golden SAML hit the headlines after the SolarWinds breach, and this post breaks down how powerful it can be. The three custom tools they mention are not public.</li>
<li><a href="https://grimmie.net/tools-techniques-and-grimmie-experimenting-w-offensive-adsi/" target="_blank">Tools, Techniques, and Grimmie?: Experimenting w/ Offensive ADSI</a>. Did you know there was a built in AD enumeration tool as far back as Windows 7 called adsisearcher?</li>
<li><a href="https://joonas.fi/2021/08/saml-is-insecure-by-design/" target="_blank">SAML is insecure by design</a>. SAML is bad and should feel bad. Lots of good ammo in here for your next web assessment that uses SAML.</li>
<li><a href="https://blog.vincss.net/2021/08/ex007-how-playing-cs-go-helped-you-bypass-security-products.html" target="_blank">[EX007] How playing CS: GO helped you bypass security products</a>. The use of a vulnerable driver allows reading process memory from a userland helper to dump lsass while EDR watches helplessly.</li>
<li><a href="https://www.rumble.run/blog/research-dcerpc/" target="_blank">Fingerprinting Windows versions, AV, wireless cards over the network—all without authentication</a>. Rumble uses DCE/RPC UUIDs to fingerprint AV, EDR, and other software agents remotely and unauthenticated. This could be very useful for advanced red teams attempting to avoid detection.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/boku7/CobaltStrikeReflectiveLoader" target="_blank">CobaltStrikeReflectiveLoader</a> is perhaps the first public User-Defined Reflective Loader for Cobalt Strike 4.4. If you are writing your own, be ready to write a lot of assembly...</li>
<li><a href="https://github.com/ktecv2000/ProxyShell" target="_blank">ProxyShell</a> is the Exchange Server RCE (ACL Bypass + EoP + Arbitrary File Write) patched in April and May of 2021 (but not published in an advisory until July 2021). Also check out <a href="https://github.com/dmaasland/proxyshell-poc" target="_blank">proxyshell-poc</a>. See here for the technique break down: <a href="https://y4y.space/2021/08/12/my-steps-of-reproducing-proxyshell/" target="_blank">My Steps of Reproducing ProxyShell</a>.</li>
<li><a href="https://github.com/cube0x0/MiniDump" target="_blank">MiniDump</a> is a C# implementation of mimikatz/pypykatz minidump functionality to get credentials from LSASS dumps.</li>
<li><a href="https://github.com/jfmaes/LazySign" target="_blank">LazySign</a> creates fake certs for binaries using windows binaries and the power of bat files. If you're on Linux try <a href="https://github.com/Tylous/Limelighter" target="_blank">Limelighter</a>.</li>
<li><a href="https://github.com/hariomenkel/CobaltSpam" target="_blank">CobaltSpam</a> is a tool based on <a href="https://github.com/Sentinel-One/CobaltStrikeParser" target="_blank">CobaltStrikeParser</a> from SentinelOne which can be used to spam a CobaltStrike server with fake beacons.</li>
<li><a href="https://github.com/SolomonSklash/COM-Hijacking" target="_blank">COM-Hijacking</a> is an example of COM hijacking using a proxy DLL.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/raivo-otp/ios-application" target="_blank">raivo-otp / ios-application</a>. A native, lightweight and secure one-time-password (OTP) client built for iOS; Raivo OTP! Why switch from my current OTP app? See <a href="https://thalpius.com/2021/08/13/microsoft-authenticator/" target="_blank">here</a>.</li>
<li><a href="https://github.com/uxmal/reko" target="_blank">reko</a> is a decompiler for machine code binaries. If Ghidra or redare2/Rizin aren't your thing, give reko a shot.</li>
<li><a href="https://github.com/nshalabi/SysmonTools" target="_blank">SysmonTools</a> contains the following: Sysmon View: an off-line Sysmon log visualization tool, Sysmon Shell: a Sysmon configuration utility, and Sysmon Box: a Sysmon and Network capture logging utility.</li>
<li><a href="https://github.com/STMSolutions/RmiTaste" target="_blank">RmiTaste</a> allows security professionals to detect, enumerate, interact and exploit RMI services by calling remote methods with gadgets from ysoserial.</li>
<li><a href="https://github.com/REW-sploit/REW-sploit" target="_blank">REW-sploit</a> can get a shellcode/DLL/EXE, emulate the execution, and give you a set of information to help you in understanding what is going on. Example of extracted information are: API calls, encryption keys used by MSF payloads, decrypted 2nd stage coming from MSF, and Cobalt-Strike configurations (if <a href="https://github.com/Sentinel-One/CobaltStrikeParser" target="_blank">CobaltStrikeParser</a> is installed).</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
