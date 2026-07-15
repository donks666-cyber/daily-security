Title: Last Week in Security (LWiS) - 2021-05-24
Date: 2021-05-24 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-05-24
Author: Erik
Summary: CloudFlare IP filtering (<a href="https://twitter.com/vysecurity" target="_blank">@vysecurity</a>), DNSStager (<a href="https://twitter.com/mohammadaskar2" target="_blank">@mohammadaskar2</a>), Cobalt Strike OPSEC (<a href="https://twitter.com/jmoosdijk" target="_blank">@jmoosdijk</a>), Azure app phishing (<a href="https://twitter.com/nikhil_mitt" target="_blank">@nikhil_mitt</a>), decision making in red teams (<a href="https://twitter.com/Jackson_T" target="_blank">@Jackson_T</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-05-17 to 2021-05-24.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://about.gitlab.com/blog/2021/05/17/prevent-crypto-mining-abuse/" target="_blank">How to prevent crypto mining abuse on GitLab.com SaaS</a>. Cryptocurrency miners have ruined GitLab CI for the rest of us. Now even free accounts will require a credit card check, killing anonymous accounts that want to use CI/CD.</li>
<li><a href="https://www.bbc.com/news/uk-england-merseyside-57226165" target="_blank">Cheese photo leads to Liverpool drug dealer's downfall</a>. A photo of a hand holding a block of cheese was all it took to match palm and fingerprints and identify the suspect. Is this a real life case of <a href="https://www.youtube.com/watch?v=KiqkclCJsZs" target="_blank">"Enhance?"</a></li>
<li><a href="https://www.watson.ch/!313346866" target="_blank">Threema gewinnt vor Bundesgericht «gegen Überwachungsbehörden»</a>. The secure messaging app Threema does not have to provide any data to authorities, rules Swiss federal court, in a win for privacy in Europe.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="http://jackson-t.ca/ooda-loops.html" target="_blank">Operators, EDR Sensors, and OODA Loops</a>. This is a long post (full con talk), but should be required reading for any serious red team operator. Lots of people (ahem, me) can get focused on the latest exploit or technique and lose sight of process of red teaming. Hopefully this blog can serve as part of the "continual learning and growth" part of the act phase.</li>
<li><a href="https://fortynorthsecurity.com/blog/what-the-f/" target="_blank">What the F#*%</a>. The lesser known cousin of C# comes with Microsoft signed binaries that can be useful to get past application allowlisting defenses. Code available in the <a href="https://github.com/FortyNorthSecurity/What-The-F" target="_blank">What-The-F</a> repository.</li>
<li><a href="https://blog.doyensec.com//2021/05/20/graphql-csrf.html" target="_blank">That single GraphQL issue that you keep missing</a>. Bug hunters will love this post on GraphQL based CSRF. The latest release of <a href="https://github.com/doyensec/inql" target="_blank">inql</a> will help identify such issues on your next assessment or bug hunt.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2021/5/17/cve-2021-31166-a-wormable-code-execution-bug-in-httpsys" target="_blank">CVE-2021-31166: A Wormable Code Execution Bug in HTTP.sys</a>. While not as bad as it sounds, this is reachable from IIS and WinRM, so do patch! BSOD PoC: <a href="https://github.com/0vercl0k/CVE-2021-31166" target="_blank">CVE-2021-31166</a>.</li>
<li><a href="https://www.vincentyiu.com/red-team/attack-infrastructure/cloudflare-for-ip-filtering" target="_blank">CloudFlare for IP Address Filtering</a>. CloudFlare is a massive presence on the internet today, hosting over 25 million domains. In this post Vincent uses the CloudFlare firewall to block known security organizations as well as "bots" to defend his red team infrastructure.</li>
<li><a href="https://www.alteredsecurity.com/post/introduction-to-365-stealer" target="_blank">Introduction To 365-Stealer - Understanding and Executing the Illicit Consent Grant Attack</a>. This tool/technique helps an attacker create an Azure-registered application that requests access to data such as contact information, email, or documents. The attacker then tricks an end user into granting consent to the application so that the attacker can gain access to the data that the target user has access to. After the application has been granted consent, it has user account-level access to the data without the need for an organizational account. This can be defeated by admins who enable <a href="https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/tenant-restrictions" target="_blank">tenant restrictions to manage access to SaaS cloud applications</a>.</li>
<li><a href="https://shells.systems/unveiling-dnsstager-a-tool-to-hide-your-payload-in-dns/" target="_blank">Unveiling DNSStager: A tool to hide your payload in DNS</a>. With enough delay, the 59 AAAA DNS requests could easily be lost on the noise and provide the perfect way to load a lifeline beacon. They client could be modified to check a trigger (value in a GitHub gist, Twitter bio, etc) and start the process when the value changes. Be careful though DNS is one of those things that defenders are either totally blind to, or can get you caught easily if someone is watching (high entropy/high volume of unusual requests).</li>
<li><a href="https://edermi.github.io/post/2021/modding_gophish/" target="_blank">Modding Gophish</a>. Gophish has some default and unchangeable features that you may not want (X-Mailer header perhaps). This post shows how to change the 404 page as well as how to enable basic HTTP auth which may be more trusted by your targets.</li>
<li><a href="https://www.atredis.com/blog/2021/5/20/le-zeek-cest-chic-using-an-nsm-for-offense" target="_blank">Le Zeek, C’est Chic: Using an NSM for Offense</a>. The blue team's favorite tool can also be used for offense to find dual-homed machines, dns queries, and even plaintext credentials on the wire.</li>
<li><a href="https://www.microsoft.com/security/blog/2021/05/20/simuland-understand-adversary-tradecraft-and-improve-detection-strategies/" target="_blank">SimuLand: Understand adversary tradecraft and improve detection strategies</a>. SimuLand is an open-source initiative by Microsoft to help security researchers around the world deploy lab environments that reproduce well-known techniques used in real attack scenarios, actively test and verify the effectiveness of related Microsoft 365 Defender, Azure Defender, and Azure Sentinel detections, and extend threat research using telemetry and forensic artifacts generated after each simulation exercise.</li>
<li><a href="https://www.praetorian.com/blog/how-to-exploit-active-directory-acl-attack-paths-through-ldap-relaying-attacks/" target="_blank">How to Exploit Active Directory ACL Attack Paths Through LDAP Relaying Attacks</a>. This excellent post discusses two methods by which an attacker can meet the requirements of hosting an “Intranet” site, explains how an attacker can combine this scenario with Active Directory ACL attack path vulnerabilities and LDAP relaying attacks to elevate privileges, and provides a detailed walkthrough of how an operator can accomplish these tasks through Cobalt Strike.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/outflanknl/HelpColor" target="_blank">HelpColor</a>. I open the <a href="https://cobaltstrike.com/help-opsec" target="_blank">Beacon Command Behavior Survey</a> page all the time; this will be super useful for quickly seeing if I am about to fork and run! It's easy to add your own BOFs and other tools as well.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/RDPThiefInject" target="_blank">RDPThiefInject</a> is <a href="https://github.com/0x09AL/RdpThief" target="_blank">RdpThief</a> run through <a href="https://github.com/TheWover/donut" target="_blank">donut</a> and wrapped in C# to easily inject into mstsc. Convert to D/Invoke before using for better OPSEC.</li>
<li><a href="https://github.com/RedSection/OffensivePH" target="_blank">OffensivePH</a>. The older ProcessHacker driver has a lot of capabilities and may be a "known good" and thus not be detected.</li>
<li><a href="https://github.com/irsl/golang-insecureskipverify-patch" target="_blank">golang-insecureskipverify-patch</a>. If you need to inspect TLS protected communication of a black-box golang binary and it does not trust the system level CA certificates, then you can use this tool to patch the executable to act like InsecureSkipVerify was turned on. You still have some additional work, configuring a transparent proxy and setting up mitmproxy or similar.</li>
<li><a href="https://github.com/djhohnstein/macos_shell_memory" target="_blank">macos_shell_memory</a> is a CGo implementation of the initial technique put forward by <a href="https://twitter.com/ParchedMind" target="_blank">Stephanie Archibald</a> in her blog, <a href="https://blogs.blackberry.com/en/2017/02/running-executables-on-macos-from-memory" target="_blank">Running Executables on macOS From Memory</a>. It includes some convenience patches like prevent the executable's exit() call from killing the Go process.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/postrequest/link" target="_blank">link</a> is a command and control framework written in rust (cross platform) that has execute-assembly and other advanced featuers.</li>
<li><a href="https://github.com/brant-ruan/metarget" target="_blank">metarget</a> is a framework providing automatic constructions of vulnerable infrastructures.</li>
<li><a href="https://github.com/iknowjason/BlueCloud" target="_blank">BlueCloud</a> is a project for cyber range deployment including Velociraptor + HELK system with a Windows VM for security testing and R&amp;D with Azure and AWS terraform support.</li>
<li><a href="https://github.com/scythe-io/in-memory-cpython" target="_blank">in-memory-cpython</a> is a mod of cpython that can be run entirely from memory for use in offensive or defensive tooling.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
