<script lang="ts">
	// import { DefaultService } from "$lib/openapi";
    import { ScanQRCode } from "@kuiper/svelte-scan-qrcode";

    let result = "";;

    function _onPermissionError() {
        alert("Permission rejected");
        location.reload();
    }
    
    // function _onResulted() {
    //     if (1){
    //         const response = DefaultService.rootScanGet({query:{qr_code:result}}).then((v) => {
    //             alert(v.data)
    //         })
    //     }
    // }
       
</script>

<ScanQRCode
    bind:scanResult={result}
    enableQRCodeReaderButton={true}
    options={{
        onPermissionError: () => _onPermissionError(),
        // onResulted: () => _onResulted(),
    }}
/>