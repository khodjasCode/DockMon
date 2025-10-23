async function loadContainers() {
    try {
        const res = await fetch('/containers');
        const data = await res.json();

        const tbody = document.getElementById('container-table');
        tbody.innerHTML = '';

        if (data.length === 0) {
            tbody.innerHTML = `<tr><td colspan="3" class="text-center">Нет контейнеров</td></tr>`;
            return;
        }

        data.forEach(c => {
            const row = `
                <tr>
                    <td>${c.name}</td>
                    <td>${c.status}</td>
                    <td>${c.ports || '—'}</td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
    } catch (err) {
        console.error(err);
    }
}

loadContainers();
setInterval(loadContainers, 5000);

