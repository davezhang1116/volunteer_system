document.addEventListener('DOMContentLoaded', () => {
    const volunteersList = document.getElementById('volunteers-list');
    const doctorsList = document.getElementById('doctors-list');
    const careCoordinatorsList = document.getElementById('care-coordinators-list');
    const residentsList = document.getElementById('residents-list');
    const matchesContainer = document.getElementById('matches-container');

    const fetchData = async (url, listElement) => {
        const response = await fetch(url);
        const data = await response.json();
        listElement.innerHTML = '';
        data.forEach(item => {
            const li = document.createElement('li');
            li.className = 'py-1 border-b border-gray-100 last:border-b-0';

            const typeMap = {
                '/volunteers': 'volunteer',
                '/doctors': 'doctor',
                '/care-coordinators': 'care_coordinator',
                '/residents': 'resident'
            };

            if (typeMap[url]) {
                const link = document.createElement('a');
                link.href = `/admin/${typeMap[url]}/${item.id}`;
                link.className = 'text-blue-600 hover:text-blue-800 hover:underline font-medium';
                link.textContent = item.name;
                li.appendChild(link);
            } else {
                li.textContent = item.name;
            }
            listElement.appendChild(li);
        });
    };

    const fetchAllData = () => {
        if (volunteersList) {
            fetchData('/volunteers', volunteersList);
        }
        if (doctorsList) {
            fetchData('/doctors', doctorsList);
        }
        if (careCoordinatorsList) {
            fetchData('/care-coordinators', careCoordinatorsList);
        }
        if (residentsList) {
            fetchData('/residents', residentsList);
        }
    };

    const fetchMatches = async () => {
        if (!matchesContainer) return;
        const response = await fetch('/match', { method: 'POST' });
        const matches = await response.json();

        let html = '';
        const currentRole = matches.current_role;

        if (matches.doctor_matches && matches.doctor_matches.length > 0) {
            const summaryText = currentRole === 'doctor' ? 'Volunteer Matches' : 'Doctor Matches';
            html += `
                <details class="mb-2" open>
                    <summary class="text-xl font-semibold mb-3 text-gray-800 cursor-pointer select-none hover:text-blue-600 transition outline-none">${summaryText}</summary>
                    <ul class="list-disc pl-5 mb-6 space-y-2">
                        ${matches.doctor_matches.map(match => {
                if (currentRole === 'doctor') {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('volunteer', ${match.volunteer_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.volunteer}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                } else {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('doctor', ${match.doctor_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.doctor}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                }
            }).join('')}
                    </ul>
                </details>
            `;
        }
        if (matches.resident_matches && matches.resident_matches.length > 0) {
            const summaryText = currentRole === 'resident' ? 'Volunteer Matches' : 'Resident Matches';
            html += `
                <details class="mb-2" open>
                    <summary class="text-xl font-semibold mb-3 text-gray-800 cursor-pointer select-none hover:text-blue-600 transition outline-none">${summaryText}</summary>
                    <ul class="list-disc pl-5 space-y-2 mb-6">
                        ${matches.resident_matches.map(match => {
                if (currentRole === 'resident') {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('volunteer', ${match.volunteer_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.volunteer}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                } else {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('resident', ${match.resident_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.resident}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                }
            }).join('')}
                    </ul>
                </details>
            `;
        }
        if (matches.care_coordinator_matches && matches.care_coordinator_matches.length > 0) {
            const summaryText = currentRole === 'care_coordinator' ? 'Volunteer Matches' : 'Care Coordinator Matches';
            html += `
                <details class="mb-2" open>
                    <summary class="text-xl font-semibold mb-3 text-gray-800 cursor-pointer select-none hover:text-blue-600 transition outline-none">${summaryText}</summary>
                    <ul class="list-disc pl-5 space-y-2">
                        ${matches.care_coordinator_matches.map(match => {
                if (currentRole === 'care_coordinator') {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('volunteer', ${match.volunteer_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.volunteer}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                } else {
                    return `<li class="text-gray-700"><a href="javascript:void(0)" onclick="fetchUserMatchDetails('care_coordinator', ${match.care_coordinator_id})" class="font-medium text-blue-600 hover:text-blue-800 hover:underline">${match.care_coordinator}</a> <span class="text-sm text-gray-500 ml-2">(Score: <span class="font-bold text-blue-600">${match.score.toFixed(2)}</span>)</span></li>`;
                }
            }).join('')}
                    </ul>
                </details>
            `;
        }
        if (!html) {
            html = '<p class="text-gray-500 italic">No matches available at this time.</p>';
        }
        matchesContainer.innerHTML = html;
    };

    fetchAllData();
    fetchMatches();

    window.fetchUserMatchDetails = async (type, id) => {
        const container = document.getElementById('user-match-details-container');
        const title = document.getElementById('user-match-details-title');
        const content = document.getElementById('user-match-details-content');

        if (!container || !title || !content) return;

        container.classList.remove('hidden');
        container.classList.add('flex');
        content.innerHTML = '<p class="text-gray-500 animate-pulse">Loading details...</p>';

        try {
            let endpoint = '';
            if (type === 'doctor') endpoint = `/doctors/${id}`;
            else if (type === 'resident') endpoint = `/residents/${id}`;
            else if (type === 'care_coordinator') endpoint = `/care-coordinators/${id}`;
            else if (type === 'volunteer') endpoint = `/volunteers/${id}`;

            const response = await fetch(endpoint);
            const data = await response.json();

            title.textContent = `${data.name} - Details`;

            let detailsHtml = '';
            if (type === 'doctor') {
                detailsHtml += `<p><strong>Specialty:</strong> ${data.specialty || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Current Projects:</strong> ${data.current_projects || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Required Skills:</strong> ${data.required_skills || 'N/A'}</p>`;
            } else if (type === 'resident') {
                detailsHtml += `<p><strong>Life History:</strong> ${data.life_history || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Hobbies:</strong> ${data.hobbies || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Cognitive Profile:</strong> ${data.cognitive_profile || 'N/A'}</p>`;
            } else if (type === 'care_coordinator') {
                detailsHtml += `<p><strong>Facility Programs:</strong> ${data.facility_programs || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Shift Requirements:</strong> ${data.shift_requirements || 'N/A'}</p>`;
            } else if (type === 'volunteer') {
                detailsHtml += `<p><strong>Major:</strong> ${data.major || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Skills:</strong> ${data.skills || 'N/A'}</p>`;
                detailsHtml += `<p><strong>Availability:</strong> ${data.availability || 'N/A'}</p>`;
            }
            content.innerHTML = detailsHtml;
        } catch (error) {
            content.innerHTML = '<p class="text-red-500">Error loading details.</p>';
        }
    };

    const linkedStatusElements = document.querySelectorAll('.linked-status');
    const isTailwind = document.querySelector('script[src*="tailwindcss"]') !== null;
    const isAdmin = document.querySelector('a[href="/admin"]') !== null || window.location.pathname.startsWith('/admin');

    linkedStatusElements.forEach(el => {
        const text = el.textContent.trim();
        if (!text || text === 'None') return;

        const userId = el.dataset.userId;
        const entityType = el.dataset.entityType;

        const parts = text.split(',').map(p => p.trim());
        el.innerHTML = '';

        parts.forEach((part, index) => {
            const match = part.match(/Matched with (.+) \((.+)\)/);
            if (match) {
                const name = match[1];
                const role = match[2];

                const badge = document.createElement('span');
                if (isTailwind) {
                    badge.className = 'inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800 border border-indigo-200 shadow-sm mx-1';
                } else {
                    badge.className = 'badge bg-info text-dark mx-1 text-decoration-none';
                }

                const nameElement = isAdmin ? document.createElement('a') : document.createElement('span');
                if (isAdmin) {
                    nameElement.href = `/admin?search=${encodeURIComponent(name)}`;
                    nameElement.className = isTailwind ? 'hover:text-indigo-900 hover:underline font-bold' : 'text-dark text-decoration-none fw-bold';
                } else {
                    nameElement.className = isTailwind ? 'font-bold' : 'fw-bold';
                }
                nameElement.textContent = name;

                const roleSpan = document.createElement('span');
                roleSpan.className = isTailwind ? 'text-xs text-indigo-600 opacity-80' : 'text-muted ms-1 small';
                roleSpan.textContent = `(${role})`;

                badge.appendChild(nameElement);
                badge.appendChild(roleSpan);

                if (isAdmin && userId && entityType) {
                    const unlinkForm = document.createElement('form');
                    unlinkForm.method = 'POST';
                    unlinkForm.action = `/admin/unlink_specific/${entityType}/${userId}`;
                    unlinkForm.className = 'inline-block m-0 p-0 ml-1';

                    const nameInput = document.createElement('input');
                    nameInput.type = 'hidden';
                    nameInput.name = 'target_name';
                    nameInput.value = name;
                    unlinkForm.appendChild(nameInput);

                    const roleInput = document.createElement('input');
                    roleInput.type = 'hidden';
                    roleInput.name = 'target_role';
                    roleInput.value = role;
                    unlinkForm.appendChild(roleInput);

                    const unlinkBtn = document.createElement('button');
                    unlinkBtn.type = 'submit';
                    unlinkBtn.innerHTML = '&times;';
                    unlinkBtn.title = `Unlink ${name}`;
                    unlinkBtn.className = isTailwind
                        ? 'text-red-500 hover:text-red-700 focus:outline-none font-bold align-middle leading-none px-1 rounded hover:bg-red-50 transition-colors'
                        : 'btn-close ms-1 align-middle';
                    unlinkBtn.style.fontSize = isTailwind ? '1.1em' : '0.5em';
                    unlinkBtn.onclick = (e) => { if (!confirm(`Are you sure you want to unlink ${name}?`)) e.preventDefault(); };

                    unlinkForm.appendChild(unlinkBtn);
                    badge.appendChild(unlinkForm);
                }
                el.appendChild(badge);
            } else {
                const span = document.createElement('span');
                span.textContent = part;
                span.className = 'mx-1';
                el.appendChild(span);
            }
        });
    });
});
