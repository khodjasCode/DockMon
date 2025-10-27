function viewStats(containerId) {
    window.location.href = `/stats/${containerId}`;
}

document.addEventListener('DOMContentLoaded', async () => {
    const tableBody = document.getElementById('container-table');
    const searchInput = document.getElementById('search');

    async function loadContainers() {
        const response = await fetch('/containers');
        const containers = await response.json();
        renderTable(containers);

        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const filtered = containers.filter(c => {
                return query.length < 4 || c.name.toLowerCase().includes(query);
            });
            renderTable(filtered);
        });
    }

    function renderTable(containers) {
        tableBody.innerHTML = '';
        containers.forEach(c => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${c.name}</td>
                <td class="${c.status === 'running' ? 'running' : 'exited'}">${c.status}</td>
                <td>${c.ports || '—'}</td>
                <td><button onclick="viewStats('${c.id}')">Подробнее</button></td>
            `;
            tableBody.appendChild(row);
        });
    }

    await loadContainers();
});

