"""Populate client.example.json with all SUBPAGE_N_* tokens for the LA plumbing demo.
Merges new tokens into the existing JSON. Run once after editing.
"""
import json, pathlib
ROOT = pathlib.Path(__file__).parent
EX = ROOT / 'client.example.json'

cfg = json.loads(EX.read_text(encoding='utf-8'))

# Shared subpage process headline
cfg['SUBPAGE_PROCESS_HEADLINE'] = 'How we run every job'

# Per-service deep-dive content (plumbing-flavored for the LA demo)
SUBPAGES = {
    1: {  # Leak Detection
        'name': 'Leak Detection',
        'hero_headline': 'Find the leak. Fix the leak.',
        'hero_body': 'Slab leaks, pinhole leaks, wall and ceiling drips. We locate the source with thermal imaging and acoustic equipment, then repair it with the smallest opening possible.',
        'section_headline': 'Every kind of leak we handle',
        'details': [
            ('Slab leaks', 'Hot or cold water lines under your foundation. Located non-invasively, then accessed and rerouted with copper or PEX.'),
            ('Pinhole leaks', 'Hairline corrosion holes in copper supply lines. We patch or repipe the affected run, depending on the age of the system.'),
            ('Wall and ceiling leaks', 'Damp drywall, brown stains, dripping ceilings. We trace the line back to the source before opening anything up.'),
            ('Outdoor and irrigation leaks', 'Wet patches in the yard, sky-high water bills. Pressure-test the main line, isolate the break, repair without trenching the whole property.'),
            ('Pool and spa leaks', 'Losing more water than evaporation explains. Dye testing and equipment inspection to isolate plumbing vs. shell leaks.'),
            ('Gas leaks', 'Smell of gas, hissing near appliances. We test the line, find the source, and re-pipe to code, permitted and inspected.'),
        ],
        'price_headline': 'What leak detection costs in LA',
        'price_intro': 'Most leak detection visits run $300–$650 for the locate, then a separate flat-rate quote for the repair. We tell you both numbers before we start anything.',
        'price_factors': [
            'Where the leak is (above-slab vs. under-slab vs. behind tile)',
            'How accessible the line is (single story vs. multi-story, crawlspace vs. concrete)',
            'Pipe material (copper, galvanized, PEX) and what repair method makes sense',
            'Whether the repair needs drywall or tile reopened and patched',
            'Whether a permit is required (most repipes are; spot repairs usually aren\'t)',
        ],
        'price_outro': 'Insurance often covers the leak damage (drying, drywall, flooring) even when it doesn\'t cover the repair itself. We can write the report your adjuster needs.',
        'faqs': [
            ('How do you find a leak you can\'t see?',
             'Thermal imaging cameras read the temperature difference where hot water is leaking under concrete. Acoustic listening discs pick up the sound of pressurized water escaping a pipe. For irrigation, we pressure-isolate sections of line until the pressure drops where the break is.'),
            ('Will you have to break my wall or floor?',
             'Sometimes, but only the smallest opening needed. We map the leak precisely before any demolition. Often we can run a new line through the attic or wall cavity and bypass the broken section entirely, leaving the damaged pipe in place but isolated.'),
            ('How long does it take?',
             'Locate is usually 1–2 hours. The repair itself ranges from same-day (for a fitting or short run) to 2–3 days (for a slab leak that requires a reroute or a partial repipe).'),
            ('Do you do the drywall and tile repair too?',
             'We patch drywall to a primed-ready state as part of the job. We don\'t do finish paint or tile work, but we\'ll recommend a trusted local trade for the cosmetic side, or coordinate with whoever you already use.'),
        ],
        'cta_headline': 'Suspect a leak? Call now.',
        'cta_body': 'Every hour you wait, more water lands in places it shouldn\'t. We dispatch leak techs 24/7 across LA County.',
    },
    2: {  # Repiping
        'name': 'Repiping',
        'hero_headline': 'New pipes, new house.',
        'hero_body': 'Full-home repipes in copper or PEX-A. We coordinate the demo, the repipe, and the wall patching so your house comes back better than we found it, usually in 3–5 days.',
        'section_headline': 'Every kind of repipe',
        'details': [
            ('Full-house copper', 'Type-L copper supply lines throughout. The traditional, premium option. 50+ year lifespan.'),
            ('Full-house PEX-A', 'Flexible PEX runs with fewer fittings (fewer leak points). Faster install, lower material cost, 25+ year warranty.'),
            ('Partial repipes', 'Just the corroded section, just the hot lines, just one bathroom. When a full repipe isn\'t needed yet.'),
            ('Galvanized replacement', 'Old galvanized supply lines from the 1950s/60s have a 50–70 year lifespan. If yours are rust-colored at the cuts, it\'s time.'),
            ('Polybutylene removal', 'Gray "poly" plastic from the 80s/90s is failure-prone. Insurance often won\'t cover damage from poly failure, so we recommend replacement.'),
            ('Drain and waste re-piping', 'Cast iron drains that are flaking or root-infested. PVC or ABS replacement, trenchless where possible.'),
        ],
        'price_headline': 'What a repipe costs in LA',
        'price_intro': 'A full-house PEX repipe in a typical 3-bed, 2-bath LA home runs $5,500–$9,500. Copper runs $8,500–$14,000 for the same house. We\'ll quote your specific home after a walkthrough.',
        'price_factors': [
            'Square footage and number of fixtures',
            'Single-story vs. two-story (more vertical runs = more cost)',
            'Attic vs. crawlspace access (attic is usually faster)',
            'Material — PEX-A vs. copper Type L',
            'Drywall and patch scope (we patch to primed; finish paint is separate)',
        ],
        'price_outro': 'Permits and inspection are included in our repipe pricing — never charged extra. We pull the permit, schedule the inspector, and walk it through.',
        'faqs': [
            ('How long will my water be off?',
             'Each day, water is off for 6–8 hours while we\'re actively working. We restore service every evening so you can shower and use the bathrooms overnight. The whole job typically takes 3–5 working days end to end.'),
            ('PEX or copper — which should I pick?',
             'Both are excellent. Copper is the premium long-life option (50+ years) and resists UV exposure. PEX-A is faster to install, more freeze-tolerant, and easier to repair. For most LA homes we recommend PEX-A unless the buyer specifically wants copper.'),
            ('Will my walls look like swiss cheese?',
             'No. We minimize cuts by working through the attic and existing fixture openings. Where we do have to cut, we patch the drywall to a primed-ready state. Most homeowners do a single touch-up paint pass after.'),
            ('Do I have to move out?',
             'Almost never. We work in stages so at least one bathroom and the kitchen stay functional each night. Larger families sometimes opt for a hotel mid-week, but it\'s not required.'),
        ],
        'cta_headline': 'Ready to repipe?',
        'cta_body': 'Free in-home walkthrough, written flat-rate quote within 48 hours. No high-pressure sales.',
    },
    3: {  # Emergency
        'name': '24/7 Emergency',
        'hero_headline': 'Water everywhere? We\'re 60 minutes out.',
        'hero_body': 'Burst pipes, sewer backups, overflowing toilets, gas smells. We dispatch a licensed tech 24/7 anywhere in LA County, with a 60-minute target arrival.',
        'section_headline': 'Emergencies we handle right now',
        'details': [
            ('Burst supply line', 'Main shutoff first, repair second. Bring a wet vac and a smile. Most bursts are repaired same-visit.'),
            ('Sewer backup', 'Toilets gurgling, drains overflowing, basement filling. We snake or jet from the cleanout, get flow restored, then camera the line.'),
            ('Overflowing toilet', 'Wax ring failure, blocked drain, or stuck float valve. We diagnose at the door, stop the overflow, fix the underlying issue.'),
            ('Gas leak or gas smell', 'Shut off, locate, repair, re-pressurize, leak-test, inspect. We coordinate with SoCalGas when the meter is involved.'),
            ('Water heater failure', 'Tank rupture, pilot won\'t stay lit, no hot water. Diagnose on-site, repair if possible or replace within 24 hours.'),
            ('Frozen / burst hose bib', 'Yes, even in LA. Rare cold snaps split outdoor faucets. We replace with frost-resistant bibs.'),
        ],
        'price_headline': 'What an emergency call costs',
        'price_intro': 'After-hours service call: $145 (waived if you book the repair with us). Repair itself is flat-rate, quoted before any work starts.',
        'price_factors': [
            'Time of day (standard hours vs. nights / weekends / holidays)',
            'Severity (single shutoff vs. flood mitigation)',
            'Whether the cause is found and fixed in one visit, or requires followup',
            'Materials needed (we stock common parts on the truck)',
            'Whether a permit and re-inspection is needed (gas lines almost always)',
        ],
        'price_outro': 'We don\'t change the price between the quote and the invoice. If we hit something unexpected mid-repair, we stop and re-quote — your choice whether to proceed.',
        'faqs': [
            ('How fast can you really be here?',
             'Our published target is 60 minutes within LA County, 24/7. In practice we average closer to 35–45 minutes in central LA, and 60–90 minutes for the far edges (Long Beach, Pasadena, Marina del Rey). Call and we\'ll give you a real ETA based on current dispatch.'),
            ('What should I do before you arrive?',
             'Find your main water shutoff (usually street-side near the meter, or where the main enters the house) and turn it off clockwise. For toilets, the shutoff is behind the toilet on the wall. For water heaters, there\'s a cold inlet valve on top. Don\'t use water until we say it\'s safe.'),
            ('Do you charge extra at night?',
             'After-hours service call ($145) applies between 8pm and 6am, weekends, and holidays. Repair pricing itself is the same as normal hours — we don\'t mark up the work.'),
            ('Do you handle insurance claims?',
             'Yes. We document the scene with photos, write a repair report that satisfies most insurers, and can coordinate directly with your adjuster. Drying and restoration after the leak is typically a separate trade (we recommend a few good ones).'),
        ],
        'cta_headline': 'Don\'t wait. Call now.',
        'cta_body': 'Phones answered 24/7. A real dispatcher, not a robot.',
    },
    4: {  # Drain Cleaning
        'name': 'Drain Cleaning',
        'hero_headline': 'Clears that actually stay clear.',
        'hero_body': 'Snaking, hydro jetting, and sewer cameras. We clear the blockage, then show you exactly why it happened so it doesn\'t happen again next month.',
        'section_headline': 'Every kind of drain we clear',
        'details': [
            ('Kitchen sinks', 'Grease, food residue, soap buildup. Snaking handles most; recurring clogs get the jetter.'),
            ('Bathroom sinks and tubs', 'Hair, soap, mineral scale. Quick fix, $-friendly visits.'),
            ('Toilets', 'Diagnose the cause (foreign object vs. wax ring vs. main line) before we snake. Sometimes the answer is to pull the toilet.'),
            ('Main sewer lines', 'Tree roots, decades of grease, collapsed sections. Camera first, then jet or repair as needed.'),
            ('Floor drains and laundry lines', 'Lint buildup, P-trap issues. Often a quick clear with an auger or wet/dry vac.'),
            ('Sewer camera inspection', '4K live video down the line so you can see the problem yourself. Useful for purchases, insurance, and city compliance.'),
        ],
        'price_headline': 'What drain cleaning costs',
        'price_intro': 'Simple sink or shower snake: $145–$225. Toilet auger: $185. Main-line snake through a cleanout: $295. Hydro jetting: $450–$850 depending on length and severity.',
        'price_factors': [
            'Which drain (lateral fixture vs. main line)',
            'Access (existing cleanout vs. pulling a toilet vs. roof vent)',
            'Method (snake / cable vs. hydro jetter)',
            'Camera inspection (included on main-line jet jobs)',
            'Length of run (50 ft. vs. 150+ ft. to the city tap)',
        ],
        'price_outro': 'If the camera finds a broken or collapsed section, we\'ll quote the repair separately. We never push a repair you don\'t need — about 70% of drains we clear are just maintenance.',
        'faqs': [
            ('Snaking vs. hydro jetting — what\'s the difference?',
             'A snake (cable) punches a hole through the blockage. Fast and cheap, but residue stays on the pipe walls. Hydro jetting blasts pressurized water (3,000+ PSI) to scour the pipe back to bare wall. For recurring clogs or grease/root buildup, jetting lasts much longer.'),
            ('Will jetting damage my old pipes?',
             'For cast iron and clay pipes in good condition, no. For very old or already-cracked sections, we camera first and recommend a milder approach. Modern jetters have adjustable pressure for old lines.'),
            ('Do you offer warranties on a clear?',
             'Yes. Fixture drain clears: 30 days. Main-line clears: 90 days. If the same line clogs again in that window, we re-clear for free (assuming nothing structural changed).'),
            ('Should I do tree root treatment?',
             'If we find roots in your line, we recommend a foaming root killer (RootX or equivalent) every 6 months. Costs ~$30, takes 5 minutes, prevents the next backup. For aggressive trees you may eventually need a section repair.'),
        ],
        'cta_headline': 'Drain backing up? Call now.',
        'cta_body': 'Most clears done in under 90 minutes. Camera inspection included on main-line jobs.',
    },
    5: {  # Water Heater
        'name': 'Water Heater',
        'hero_headline': 'Hot water, sorted.',
        'hero_body': 'Repair, replacement, and new installs. Tank, tankless, hybrid, gas, or electric. We carry the common parts on the truck so most repairs happen on the first visit.',
        'section_headline': 'Every water heater service',
        'details': [
            ('Repair', 'Pilot won\'t light, thermocouple, gas valve, thermostat, anode rod, T&P valve. Most repairs done same-day.'),
            ('Replacement (tank)', '40, 50, or 75-gallon gas or electric. Standard install in 3–5 hours including disposal of the old unit.'),
            ('Tankless conversion', 'Switch from tank to on-demand. Gas line resize and venting work included. Endless hot water, smaller footprint, lower utility bills.'),
            ('Hybrid heat pump install', 'Heat pump water heaters cut electric water heating bills 50–70%. Federal tax credit + LADWP rebate often available.'),
            ('Recirculation pump', 'Hot water at the far bathroom in 5 seconds instead of 90. Saves water and reduces wait time.'),
            ('Annual flush and inspection', 'Drains sediment from the tank, extends life by years. Anode rod inspection. Bundle with HVAC tune-up season.'),
        ],
        'price_headline': 'What a water heater costs',
        'price_intro': 'Standard 50-gallon gas tank install: $1,650–$2,200 including the unit. Tankless conversion: $4,200–$6,500 depending on gas line work. Heat pump hybrid: $3,500–$5,500 (rebates can knock $1,000+ off).',
        'price_factors': [
            'Tank vs. tankless vs. hybrid',
            'Capacity (40 / 50 / 75 / 80 gallon)',
            'Gas or electric (gas often cheaper to run, electric often cheaper to install)',
            'Venting and gas line modifications needed',
            'Code upgrades required (expansion tank, seismic straps, pan and drain)',
        ],
        'price_outro': 'Permits and inspection are included on every water heater install — never charged extra. Most rebates we file for you directly.',
        'faqs': [
            ('How long does a water heater last in LA?',
             'Standard tank: 8–12 years with regular flushing, 6–8 without. Tankless: 15–20 years. Hybrid heat pump: 12–15 years. LA water has moderate hardness, which is hard on tanks — annual flushing makes a real difference.'),
            ('Tank or tankless — which should I buy?',
             'If you have 2+ people who shower back-to-back or a hot tub, tankless pays off. If you\'re a 1–2 person household with normal usage, a high-efficiency tank is often the better value. We don\'t push tankless unless the math works for your house.'),
            ('Can I do a heat pump in my garage?',
             'Yes, and the LADWP rebate is significant. Heat pumps need ~700 cubic feet of air around them and exhaust cool air — perfect for a garage. We handle the rebate paperwork.'),
            ('My water heater is leaking — repair or replace?',
             'If the leak is from a fitting, valve, or T&P, repair. If the leak is from the tank itself (bottom seam), it\'s done — replace. We can tell which it is on-site in under 10 minutes.'),
        ],
        'cta_headline': 'No hot water? We\'re on it.',
        'cta_body': 'Most water heater repairs same-day. Replacements within 24 hours.',
    },
}

for n, s in SUBPAGES.items():
    cfg[f'SUBPAGE_{n}_HERO_HEADLINE'] = s['hero_headline']
    cfg[f'SUBPAGE_{n}_HERO_BODY'] = s['hero_body']
    cfg[f'SUBPAGE_{n}_SECTION_HEADLINE'] = s['section_headline']
    for i, (title, body) in enumerate(s['details'], start=1):
        cfg[f'SUBPAGE_{n}_DETAIL_{i}_TITLE'] = title
        cfg[f'SUBPAGE_{n}_DETAIL_{i}_BODY'] = body
    cfg[f'SUBPAGE_{n}_PRICE_HEADLINE'] = s['price_headline']
    cfg[f'SUBPAGE_{n}_PRICE_INTRO'] = s['price_intro']
    for i, factor in enumerate(s['price_factors'], start=1):
        cfg[f'SUBPAGE_{n}_PRICE_FACTOR_{i}'] = factor
    cfg[f'SUBPAGE_{n}_PRICE_OUTRO'] = s['price_outro']
    for i, (q, a) in enumerate(s['faqs'], start=1):
        cfg[f'SUBPAGE_{n}_FAQ_{i}_Q'] = q
        cfg[f'SUBPAGE_{n}_FAQ_{i}_A'] = a
    cfg[f'SUBPAGE_{n}_CTA_HEADLINE'] = s['cta_headline']
    cfg[f'SUBPAGE_{n}_CTA_BODY'] = s['cta_body']

EX.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'updated client.example.json — {len(cfg)} tokens total')
