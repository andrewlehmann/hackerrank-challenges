import java.util.*;
import java.util.stream.*;

public static int totalAssetValues(final List<Asset> assets) {
  return assets.stream()
               .mapToInt(Asset::getValue)
               .sum();
}

final List<Asset> assets = Arrays.asList(
  new Asset(Asset.AssetType.BOND, 1000),
  new Asset(Asset.AssetType.BOND, 2000),
  new Asset(Asset.AssetType.STOCK, 3000),
  new Asset(Asset.AssetType.Stock, 4000)
);

System.out.println("Total of all assets: " + totalAssetValues(assets));
      
