function onclickEditReport(reportId) {
    // Redirects to the update view
    window.location.href = '/report/' + reportId;
}

function onclickDeleteReport(reportId) {
    // Redirects to the deletion view (GET method as per Waypoint 9)
    window.location.href = '/report/' + reportId + '/deletion';
}

function onclickAddReport() {
    // Redirects to the creation view
    window.location.href = '/report';
}
