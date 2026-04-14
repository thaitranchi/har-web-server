function onclickEditReport(reportId) {
    window.location.href = '/report/' + reportId;
}

function onclickDeleteReport(reportId) {
    // Waypoint 9 often uses a simple GET redirect for deletion
    if (confirm('Are you sure you want to delete this report?')) {
        window.location.href = '/report/' + reportId + '/deletion';
    }
}

function onclickAddReport() {
    window.location.href = '/report';
}
