Title: Last Week in Security (LWiS) - 2023-03-07
Date: 2023-03-07 21:40
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-03-07
Author: Erik
Summary: Cobalt Strike 4.8 (<a href="https://twitter.com/gregdarwin" target="_blank">@gregdarwin</a>), Timeroasting, Mythic 3.0 (<a href="https://twitter.com/its_a_feature_/" target="_blank">@its_a_feature_</a>), LastPass breach saga continues, CosmosDB XSS to account takeover (<a href="https://twitter.com/creastery" target="_blank">@Creastery</a>), 😈 chrome extension (<a href="https://twitter.com/mattfriz" target="_blank">@mattfriz</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past 2 weeks. This post covers 2023-02-20 to 2023-03-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-4-8-system-call-me-maybe/" target="_blank">Cobalt Strike 4.8: (System) Call Me Maybe</a>. Some great new features (multi-byte XOR for DLL loading), and bug fixes including the age old impersonation bug (that would always say "Impersonated &lt;current user&gt;"). Welcome changes in a competitive landscape.</li>
<li><a href="https://docs.mythic-c2.net/v/version-3.0/updating/mythic-2.3-greater-than-3.0-updates" target="_blank">Mythic 2.3 -&gt; 3.0 Updates</a>. Not to be left behind, Mythic is moving to 3.0 with an all new Go backend.</li>
<li><a href="https://security.googleblog.com/2023/03/google-trust-services-now-offers-tls.html" target="_blank">Google Trust Services now offers TLS certificates for Google Domains customers</a>. Google Domains customers can now use DNS-01 challenges to get certificates!</li>
<li><a href="https://palant.info/2023/02/28/lastpass-breach-update-the-few-additional-bits-of-information/" target="_blank">LastPass breach update: The few additional bits of information</a>. The saga continues. A Plex Media Server RCE on a DevOps engineer's home computer led to the theft of all LasPass data. This should have been stopped at a few different levels, and they subtle blame shift to the engineer isn't good. You have to assume that any device you don't control is fully compromised and monitor access from it appropriately (or deny it).</li>
<li><a href="https://portswigger.net/daily-swig/were-going-teetotal-its-goodbye-to-the-daily-swig" target="_blank">We're going teetotal: It's goodbye to The Daily Swig</a>. Pour one out for this great news source.</li>
<li><a href="https://www.vice.com/en/article/dy7axa/how-i-broke-into-a-bank-account-with-an-ai-generated-voice" target="_blank">How I Broke Into a Bank Account With an AI-Generated Voice</a>. I've been warning about this for a while. Even <a href="https://www.imdb.com/title/tt0105435/" target="_blank">Sneakers (1992)</a> showed how easy voice based authentication was to spoof.</li>
<li><a href="https://krebsonsecurity.com/2023/03/highlights-from-the-new-u-s-cybersecurity-strategy/" target="_blank">Highlights from the New U.S. Cybersecurity Strategy</a>. Grab the highlights here or dig into the <a href="https://www.whitehouse.gov/wp-content/uploads/2023/03/National-Cybersecurity-Strategy-2023.pdf" target="_blank">full PDF</a>.</li>
<li><a href="https://techcrunch.com/2023/02/21/sensitive-united-states-military-emails-spill-online/" target="_blank">Sensitive US military emails spill online</a>. But remember, if you don't use FIPS validated and certified crypto modules, you are putting sensitive information at risk!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/cicd-secrets-extraction-tips-and-tricks.html" target="_blank">CI/CD secrets extraction, tips and tricks</a> Synacktiv drops <a href="https://github.com/synacktiv/nord-stream" target="_blank">Nord Stream</a>, a tool that allows you to list the secrets stored inside CI/CD environments and extract them by deploying malicious pipelines. It currently supports Azure DevOps and GitHub. Don't be fooled by "secret" files and "masked" variables. If the pipeline needs it to build, it can be extracted.</li>
<li><a href="https://github.blog/2023-02-23-the-code-that-wasnt-there-reading-memory-on-an-android-device-by-accident/" target="_blank">The code that wasn't there: Reading memory on an Android device by accident</a>. These low level exploits are always somewhat magic to me.</li>
<li><a href="https://frischkorn-nicholas.medium.com/red-teaming-macos-101-33b5a1834a2e" target="_blank">Red Teaming macOS 101</a>. Excellent write-up for those involved in attacking/defending MacOS assets!</li>
<li><a href="https://www.signal-labs.com/blog/windows-hotpatching-amp-process-injection" target="_blank">Windows Hotpatching &amp; Process Injection</a>. Did you know the latest Windows insider builds and Azure server ISOs can hotpatch running processes? Expect both malware and EDRs to (ab)use this feature in the future.</li>
<li><a href="https://starlabs.sg/blog/2023/02-microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer/" target="_blank">Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer</a>. Regex is hard for everyone. In this case, a single unescaped dot led to a 1-click Azure account takeover.</li>
<li><a href="https://blog.doyensec.com//2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html" target="_blank">A New Vector For “Dirty” Arbitrary File Write to RCE</a>. Lax config parsers allow arbitrary data/files to be used to "smuggle" configuration files. This technique was used with <a href="http://antirez.com/news/96" target="_blank">Redis</a> a while back.</li>
<li><a href="https://blog.nviso.eu/2023/02/27/onenote-embedded-file-abuse/" target="_blank">OneNote Embedded File Abuse</a>. Not caught up on the latest hotness (.one)? Get with the program!</li>
<li><a href="https://cloudbrothers.info/en/prem-global-admin-password-reset/" target="_blank">From on-prem to Global Admin without password reset</a>. An "On-prem to Global admin" attack path that requires quite a foothold but still good to have in your bag as it might bypass some Conditional Access configurations.</li>
<li><a href="https://www.horizon3.ai/from-cve-2022-33679-to-unauthenticated-kerberoasting/" target="_blank">From CVE-2022-33679 to Unauthenticated Kerberoasting</a>. If you missed the kerberos exploit from 2022-10, this post does a good job of introducing the concept of pre-authentication, explaining the flaw, and how to exploit it.</li>
<li><a href="https://qoop.org/publications/cve-2023-21716-rtf-fonttbl.md" target="_blank">Microsoft Word RTF Font Table Heap Corruption</a>. Just a crash PoC, but with a CVSS of 9.8, and Word 2007 to Insider Preview - 2211 Build 15831.20122 CTR affected, expect to see it in the wild soon.</li>
<li><a href="https://fortynorthsecurity.com/blog/redirecting-maldoc-transfers-in-the-cloud/" target="_blank">Maldoc Transfers in the Google Cloud</a>. Host your payloads on a high reputation Google domain (cloudfunctions.net).</li>
<li><a href="https://mattfrisbie.substack.com/p/spy-chrome-extension" target="_blank">Let's build a Chrome extension that steals everything</a>. Red teamers should have an extension like this ready to deploy as we move to a SaaS world and the browser is the only security control after initial access. Code <a href="https://github.com/msfrisbie/spy-extension" target="_blank">here</a>.</li>
<li><a href="https://skr1x.github.io/keepass-dll-hijacking/" target="_blank">Having fun with KeePass2: DLL Hijacking and hooking APIs</a>. Hooking via DLL hijacking is a powerful primitive.</li>
<li><a href="https://labs.nettitude.com/blog/introducing-aladdin/" target="_blank">Introducing Aladdin</a>. A new tool and technique for red teamers to bypass misconfigured Windows Defender Application Control (WDAC) and AppLocker. Aladdin exploits a deserialisation issue over .NET remoting in order to execute code inside addinprocess.exe, bypassing a 2019 patch released by Microsoft in .NET Framework version 4.8.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Octoberfest7/MemFiles" target="_blank">MemFiles</a> -  A CobaltStrike toolkit to write files produced by Beacon to memory instead of disk.</li>
<li><a href="https://github.com/ZeroMemoryEx/Amsi-Killer" target="_blank">Amsi-Killer</a> - a "lifetime AMSI bypass."</li>
<li><a href="https://github.com/JoelGMSec/Thunderstorm" target="_blank">Thunderstorm</a> - Modular framework to exploit UPS devices. Only 2 exploits for now.</li>
<li><a href="https://github.com/mgeeky/msidump" target="_blank">msidump</a> - a tool that analyzes malicious MSI installation packages, extracts files, streams, binary data and incorporates YARA scanner.</li>
<li><a href="https://github.com/mrexodia/lolbin-poc" target="_blank">lolbin-poc</a> - Small PoC of using a Microsoft signed executable as a lolbin.</li>
<li><a href="https://github.com/kraken-ng/Kraken" target="_blank">Kraken</a> - a modular multi-language webshell coded by @secu_x11.</li>
<li><a href="https://github.com/nccgroup/DroppedConnection" target="_blank">DroppedConnection</a> - Emulates a Cisco ASA Anyconnect VPN service, accepting any credentials (and logging them) before serving VBS to the client that gets executed in the context of the user.</li>
<li><a href="https://github.com/SecuraBV/Timeroast" target="_blank">Timeroast</a> - Scripts that execute timeroasting and trustroasting attack techniques by discovering weak computer or trust passwords within an Active Directory domain.</li>
<li><a href="https://github.com/NUL0x4C/AtomLdr" target="_blank">AtomLdr</a> -  A DLL loader with advanced evasive features.</li>
<li><a href="https://github.com/realoriginal/bootlicker" target="_blank">bootlicker</a> - A generic UEFI bootkit used to achieve initial usermode execution. It works with modifications.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/TrimarcJake/Locksmith" target="_blank">Locksmith</a>.  A tiny tool to identify and remediate common misconfigurations in Active Directory Certificate Services. Quick wins for Sysadmins!</li>
<li><a href="https://github.com/Cyber-Buddy/APKHunt" target="_blank">APKHunt</a> is a comprehensive static code analysis tool for Android apps that is based on the OWASP MASVS framework. Although APKHunt is intended primarily for mobile app developers and security testers, it can be used by anyone to identify and address potential security vulnerabilities in their code.</li>
<li><a href="https://github.com/p0dalirius/Coercer" target="_blank">Coercer</a>.  A python script to automatically coerce a Windows server to authenticate on an arbitrary machine through 12 methods. #onetorullethemall</li>
<li><a href="https://github.com/lwthiker/curl-impersonate" target="_blank">curl-impersonate</a> - A special build of curl that can impersonate Chrome &amp; Firefox.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 337 (+0)</p>
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
