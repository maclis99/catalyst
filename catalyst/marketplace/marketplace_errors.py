import sys
import traceback

from catalyst.errors import ZiplineError


def silent_except_hook(exctype, excvalue, exctraceback):
    if exctype in [MarketplacePubAddressEmpty, MarketplaceDatasetNotFound,
                   MarketplaceNoAddressMatch, MarketplaceHTTPRequest,
                   MarketplaceNoCSVFiles, MarketplaceContractDataNoMatch,
                   MarketplaceSubscriptionExpired]:
        fn = traceback.extract_tb(exctraceback)[-1][0]
        ln = traceback.extract_tb(exctraceback)[-1][1]
        print("Error traceback: {1} (line {2})\n"
              "{0.__name__}:  {3}".format(exctype, fn, ln, excvalue))
    else:
        sys.__excepthook__(exctype, excvalue, exctraceback)


sys.excepthook = silent_except_hook


class MarketplacePubAddressEmpty(ZiplineError):
    msg = (
        'Please enter your public address to use in the Data Marketplace '
        'in the following file: {filename}'
    ).strip()


class MarketplaceDatasetNotFound(ZiplineError):
    msg = (
        'The dataset "{dataset}" is not registered in the Data Marketplace.'
    ).strip()


class MarketplaceNoAddressMatch(ZiplineError):
    msg = (
        'The address registered with the dataset {dataset}: {address} '
        'does not match any of your addresses.'
    ).strip()


class MarketplaceHTTPRequest(ZiplineError):
    msg = (
        'Request to remote server to {request} failed: {error}'
    ).strip()


class MarketplaceNoCSVFiles(ZiplineError):
    msg = (
        'No CSV files found on {datadir} to upload.'
    )


class MarketplaceContractDataNoMatch(ZiplineError):
    msg = (
        'The information found on the contract does not match the '
        'requested data:\n{params}.'
    )


class MarketplaceSubscriptionExpired(ZiplineError):
    msg = (
        'Your subscription to dataset "{dataset}" expired on {date} '
        'and is no longer active. You have to subscribe again running the '
        'following command:\n'
        'catalyst marketplace subscribe --dataset={dataset}'
    )
